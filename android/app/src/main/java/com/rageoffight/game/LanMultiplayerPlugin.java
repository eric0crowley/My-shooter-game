package com.rageoffight.game;

import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.NetworkInterface;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

@CapacitorPlugin(name = "LanMultiplayer")
public class LanMultiplayerPlugin extends Plugin {

    private static final int DEFAULT_PORT = 24180;
    private static final int MAX_PLAYERS = 4;
    private static final int MAX_MESSAGE_CHARS = 24 * 1024;

    private final ExecutorService io = Executors.newCachedThreadPool();
    private final Map<String, Peer> peers = new ConcurrentHashMap<>();
    private final AtomicInteger peerSequence = new AtomicInteger(1);
    private volatile ServerSocket serverSocket;
    private volatile Socket clientSocket;
    private volatile PrintWriter clientWriter;
    private volatile boolean hostMode;

    @PluginMethod
    public void startHost(PluginCall call) {
        final int port = call.getInt("port", DEFAULT_PORT);
        if (port < 1024 || port > 65535) {
            call.reject("پورت باید بین ۱۰۲۴ و ۶۵۵۳۵ باشد.");
            return;
        }
        if (serverSocket != null && !serverSocket.isClosed()) {
            call.reject("میزبانی از قبل فعال است.");
            return;
        }
        if (clientSocket != null && !clientSocket.isClosed()) {
            call.reject("ابتدا اتصال مهمان را قطع کن.");
            return;
        }

        io.execute(() -> {
            ServerSocket server = null;
            try {
                server = new ServerSocket();
                server.setReuseAddress(true);
                server.bind(new InetSocketAddress("0.0.0.0", port), MAX_PLAYERS);
                serverSocket = server;
                hostMode = true;
                final ServerSocket activeServer = server;
                io.execute(() -> acceptClients(activeServer));

                JSObject result = new JSObject();
                result.put("address", findLocalAddress());
                result.put("port", server.getLocalPort());
                result.put("maxPlayers", MAX_PLAYERS + 1);
                call.resolve(result);
            } catch (Exception error) {
                if (server != null) {
                    try { server.close(); } catch (Exception ignored) {}
                }
                serverSocket = null;
                hostMode = false;
                call.reject("شروع میزبان شبکهٔ محلی ممکن نشد. وای‌فای را بررسی کن.", error);
            }
        });
    }

    @PluginMethod
    public void connect(PluginCall call) {
        final String host = call.getString("host");
        final int port = call.getInt("port", DEFAULT_PORT);
        if (host == null || host.trim().isEmpty()) {
            call.reject("نشانی میزبان را وارد کن.");
            return;
        }
        if (port < 1024 || port > 65535) {
            call.reject("پورت باید بین ۱۰۲۴ و ۶۵۵۳۵ باشد.");
            return;
        }
        if ((clientSocket != null && !clientSocket.isClosed()) || (serverSocket != null && !serverSocket.isClosed())) {
            call.reject("یک اتصال شبکه از قبل فعال است.");
            return;
        }

        io.execute(() -> {
            Socket socket = new Socket();
            try {
                socket.connect(new InetSocketAddress(host.trim(), port), 7000);
                socket.setTcpNoDelay(true);
                socket.setKeepAlive(true);
                PrintWriter writer = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true);
                clientSocket = socket;
                clientWriter = writer;
                hostMode = false;

                JSObject result = new JSObject();
                result.put("host", host.trim());
                result.put("port", port);
                result.put("address", findLocalAddress());
                call.resolve(result);
                notifyListeners("connected", result);
                io.execute(() -> readClient(socket));
            } catch (Exception error) {
                try { socket.close(); } catch (Exception ignored) {}
                clientSocket = null;
                clientWriter = null;
                call.reject("اتصال برقرار نشد. IP و اتصال هر دو گوشی به یک وای‌فای را بررسی کن.", error);
            }
        });
    }

    @PluginMethod
    public void send(PluginCall call) {
        JSObject message = call.getObject("message");
        if (message == null) {
            call.reject("پیام شبکه خالی است.");
            return;
        }
        String json = message.toString();
        if (json.length() > MAX_MESSAGE_CHARS) {
            call.reject("پیام شبکه بیش از حد بزرگ است.");
            return;
        }

        if (hostMode) {
            int sent = 0;
            for (Peer peer : new ArrayList<>(peers.values())) {
                if (peer.send(json)) sent++;
            }
            JSObject result = new JSObject();
            result.put("recipients", sent);
            call.resolve(result);
            return;
        }

        PrintWriter writer = clientWriter;
        if (writer == null || clientSocket == null || clientSocket.isClosed()) {
            call.reject("به میزبان شبکه متصل نیستی.");
            return;
        }
        synchronized (writer) {
            writer.println(json);
            if (writer.checkError()) {
                call.reject("ارسال پیام شبکه ناموفق بود.");
                return;
            }
        }
        call.resolve();
    }

    @PluginMethod
    public void sendTo(PluginCall call) {
        final String peerId = call.getString("peerId");
        final JSObject message = call.getObject("message");
        if (!hostMode || peerId == null || message == null) {
            call.reject("ارسال مستقیم فقط از میزبان به بازیکن متصل ممکن است.");
            return;
        }
        String json = message.toString();
        if (json.length() > MAX_MESSAGE_CHARS) {
            call.reject("پیام شبکه بیش از حد بزرگ است.");
            return;
        }
        Peer peer = peers.get(peerId);
        if (peer == null || !peer.send(json)) {
            call.reject("این بازیکن دیگر متصل نیست.");
            return;
        }
        call.resolve();
    }

    @PluginMethod
    public void stopHost(PluginCall call) {
        closeHost();
        call.resolve();
    }

    @PluginMethod
    public void disconnect(PluginCall call) {
        closeClient();
        call.resolve();
    }

    private void acceptClients(ServerSocket server) {
        while (!server.isClosed()) {
            try {
                Socket socket = server.accept();
                socket.setTcpNoDelay(true);
                socket.setKeepAlive(true);
                if (peers.size() >= MAX_PLAYERS) {
                    try { socket.close(); } catch (Exception ignored) {}
                    continue;
                }
                String id = "peer-" + peerSequence.getAndIncrement() + "-" + UUID.randomUUID().toString().substring(0, 6);
                Peer peer = new Peer(id, socket);
                peers.put(id, peer);
                JSObject event = new JSObject();
                event.put("peerId", id);
                event.put("address", socket.getInetAddress().getHostAddress());
                notifyListeners("peerConnected", event);
                io.execute(() -> readPeer(peer));
            } catch (Exception error) {
                if (!server.isClosed()) notifyError("پذیرش بازیکن شبکه ناموفق بود.");
                break;
            }
        }
    }

    private void readPeer(Peer peer) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(peer.socket.getInputStream(), StandardCharsets.UTF_8))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.length() > MAX_MESSAGE_CHARS) break;
                dispatchMessage(line, peer.id);
            }
        } catch (Exception ignored) {
            // The peer-disconnected event below carries the useful state to JS.
        } finally {
            peers.remove(peer.id);
            peer.close();
            JSObject event = new JSObject();
            event.put("peerId", peer.id);
            notifyListeners("peerDisconnected", event);
        }
    }

    private void readClient(Socket socket) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.length() > MAX_MESSAGE_CHARS) break;
                dispatchMessage(line, null);
            }
        } catch (Exception ignored) {
            // A connection-lost event is emitted in finally.
        } finally {
            if (clientSocket == socket) {
                clientSocket = null;
                clientWriter = null;
                JSObject event = new JSObject();
                event.put("reason", "connection-closed");
                notifyListeners("disconnected", event);
            }
            try { socket.close(); } catch (Exception ignored) {}
        }
    }

    private void dispatchMessage(String line, String peerId) {
        try {
            JSObject envelope = new JSObject();
            envelope.put("message", new JSObject(line));
            if (peerId != null) envelope.put("peerId", peerId);
            notifyListeners("message", envelope);
        } catch (Exception ignored) {
            // Ignore malformed packets; the stream remains usable for later messages.
        }
    }

    private void closeHost() {
        hostMode = false;
        ServerSocket server = serverSocket;
        serverSocket = null;
        if (server != null) {
            try { server.close(); } catch (Exception ignored) {}
        }
        for (Peer peer : new ArrayList<>(peers.values())) {
            peers.remove(peer.id);
            peer.close();
        }
    }

    private void closeClient() {
        Socket socket = clientSocket;
        clientSocket = null;
        clientWriter = null;
        if (socket != null) {
            try { socket.close(); } catch (Exception ignored) {}
        }
        hostMode = false;
    }

    private String findLocalAddress() {
        try {
            Enumeration<NetworkInterface> interfaces = NetworkInterface.getNetworkInterfaces();
            List<String> fallback = new ArrayList<>();
            while (interfaces != null && interfaces.hasMoreElements()) {
                NetworkInterface networkInterface = interfaces.nextElement();
                if (!networkInterface.isUp() || networkInterface.isLoopback()) continue;
                Enumeration<InetAddress> addresses = networkInterface.getInetAddresses();
                while (addresses.hasMoreElements()) {
                    InetAddress address = addresses.nextElement();
                    if (!(address instanceof Inet4Address) || address.isLoopbackAddress() || !address.isSiteLocalAddress()) continue;
                    String ip = address.getHostAddress();
                    String name = networkInterface.getName().toLowerCase();
                    if (name.startsWith("wlan") || name.startsWith("wifi")) return ip;
                    fallback.add(ip);
                }
            }
            if (!fallback.isEmpty()) return fallback.get(0);
        } catch (Exception ignored) {}
        return "127.0.0.1";
    }

    private void notifyError(String message) {
        JSObject event = new JSObject();
        event.put("message", message);
        notifyListeners("error", event);
    }

    @Override
    protected void handleOnDestroy() {
        closeHost();
        closeClient();
        io.shutdownNow();
        super.handleOnDestroy();
    }

    private static final class Peer {
        final String id;
        final Socket socket;
        private final PrintWriter writer;

        Peer(String id, Socket socket) throws Exception {
            this.id = id;
            this.socket = socket;
            this.writer = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true);
        }

        synchronized boolean send(String message) {
            if (socket.isClosed()) return false;
            writer.println(message);
            return !writer.checkError();
        }

        void close() {
            try { writer.close(); } catch (Exception ignored) {}
            try { socket.close(); } catch (Exception ignored) {}
        }
    }
}

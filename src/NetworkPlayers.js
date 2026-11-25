import * as THREE from 'three';

function createMaterial(color) {
  return new THREE.MeshStandardMaterial({ color, roughness: 0.74, metalness: 0.08 });
}

export class NetworkPlayers {
  constructor(scene) {
    this.scene = scene;
    this.actors = new Map();
  }

  createActor(id) {
    const group = new THREE.Group();
    group.userData.networkPlayerId = id;
    const color = id === 'host' ? 0x3ca9a3 : 0x528ad1;
    const body = new THREE.Mesh(new THREE.CapsuleGeometry(0.36, 0.82, 4, 8), createMaterial(color));
    body.position.y = 0.82;
    body.castShadow = true;
    const vest = new THREE.Mesh(new THREE.BoxGeometry(0.56, 0.5, 0.22), createMaterial(0x263841));
    vest.position.set(0, 0.9, 0.06);
    vest.castShadow = true;
    const head = new THREE.Mesh(new THREE.SphereGeometry(0.23, 12, 10), createMaterial(0xd5ad91));
    head.position.y = 1.55;
    head.castShadow = true;
    const rifle = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.09, 0.62), createMaterial(0x303a40));
    rifle.position.set(0.31, 1.12, 0.38);
    rifle.castShadow = true;
    group.add(body, vest, head, rifle);
    group.visible = false;
    this.scene.add(group);
    return { id, group, initialized: false, name: id === 'host' ? 'میزبان' : 'بازیکن' };
  }

  update(playerStates, localId, dt) {
    const seen = new Set();
    for (const state of playerStates || []) {
      if (!state || typeof state.id !== 'string' || state.id === localId) continue;
      const x = Number(state.x);
      const y = Number(state.y);
      const z = Number(state.z);
      const yaw = Number(state.yaw);
      if (![x, y, z, yaw].every(Number.isFinite)) continue;

      const actorId = state.id;
      seen.add(actorId);
      let actor = this.actors.get(actorId);
      if (!actor) {
        actor = this.createActor(actorId);
        this.actors.set(actorId, actor);
      }
      actor.name = typeof state.name === 'string' ? state.name.slice(0, 20) : actor.name;
      const group = actor.group;
      const target = new THREE.Vector3(x, Math.max(0, Math.min(3.5, y - 1.7)), z);
      if (!actor.initialized) {
        group.position.copy(target);
        actor.initialized = true;
      } else {
        group.position.lerp(target, Math.min(1, Math.max(0, dt) * 14));
      }
      group.rotation.y = yaw;
      group.visible = state.alive !== false;
    }

    for (const [id, actor] of this.actors) {
      if (!seen.has(id)) {
        this.scene.remove(actor.group);
        actor.group.traverse((object) => {
          object.geometry?.dispose();
          object.material?.dispose();
        });
        this.actors.delete(id);
      }
    }
  }

  clear() {
    for (const actor of this.actors.values()) {
      this.scene.remove(actor.group);
      actor.group.traverse((object) => {
        object.geometry?.dispose();
        object.material?.dispose();
      });
    }
    this.actors.clear();
  }
}

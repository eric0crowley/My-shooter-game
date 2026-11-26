const persianDigits = new Intl.NumberFormat('fa-IR', { maximumFractionDigits: 0, useGrouping: false });
const formatNumber = (value) => persianDigits.format(Math.max(0, Math.floor(value || 0)));
function formatClock(seconds = 0) {
  const total = Math.max(0, Math.ceil(Number(seconds) || 0));
  const minutes = Math.floor(total / 60);
  const remainder = total % 60;
  return `${persianDigits.format(minutes).padStart(2, '۰')}:${persianDigits.format(remainder).padStart(2, '۰')}`;
}

export class HUD {
  constructor() {
    this.healthFill = document.getElementById('health-fill');
    this.healthValue = document.getElementById('health-value');
    this.healthPanel = document.getElementById('bottom-left');
    this.ammoEl = document.getElementById('ammo');
    this.weaponEl = document.getElementById('weapon-name');
    this.scoreEl = document.getElementById('score');
    this.modeEl = document.getElementById('mode-label');
    this.matchPanel = document.getElementById('match-panel');
    this.blueScore = document.getElementById('blue-score');
    this.redScore = document.getElementById('red-score');
    this.matchClock = document.getElementById('match-clock');
    this.respawnNotice = document.getElementById('respawn-notice');
    this.respawnCountdown = document.getElementById('respawn-countdown');
    this.wavePanel = document.getElementById('wave-panel');
    this.waveValue = document.getElementById('wave-value');
    this.waveHint = document.getElementById('wave-hint');
    this.hitmarker = document.getElementById('hitmarker');
    this.damageVignette = document.getElementById('damage-vignette');
    this.hitTimer = 0;
    this.damageTimer = 0;
  }

  update(player, weapon, stats) {
    const health = Math.max(0, Math.ceil(player.health));
    const healthPercent = (health / player.maxHealth) * 100;
    this.healthFill.style.width = `${healthPercent}%`;
    this.healthValue.textContent = formatNumber(health);
    this.healthPanel.classList.toggle('low-health', healthPercent <= 30);

    this.ammoEl.innerHTML = weapon.reloading
      ? 'خشاب‌گذاری'
      : `${formatNumber(weapon.ammo)} <small>/ ${formatNumber(weapon.maxAmmo)}</small>`;
    this.weaponEl.textContent = weapon.name;
    this.scoreEl.textContent = formatNumber(stats.kills);

    const isZombie = stats.mode === 'zombie';
    const isTeamMatch = stats.mode === 'tdm';
    this.modeEl.textContent = stats.online
      ? `${isZombie ? 'بقا' : 'تمرینی'} · شبکهٔ محلی`
      : (isZombie ? 'بقا · آفلاین' : isTeamMatch ? 'مسابقهٔ تیمی' : 'تمرینی · آفلاین');
    this.matchPanel.style.display = isTeamMatch ? 'flex' : 'none';
    if (isTeamMatch) {
      const match = stats.match;
      this.blueScore.textContent = formatNumber(match?.scores?.blue);
      this.redScore.textContent = formatNumber(match?.scores?.red);
      this.matchClock.textContent = formatClock(match?.remainingSeconds);
    }
    this.wavePanel.style.display = isZombie ? 'grid' : 'none';
    if (isZombie) {
      this.waveValue.textContent = formatNumber(stats.wave);
      this.waveHint.textContent = stats.waveIntermission > 0
        ? `موج بعدی تا ${formatNumber(Math.ceil(stats.waveIntermission))} ثانیه`
        : `${formatNumber(stats.remainingCount)} زامبی باقی‌مانده`;
    }
  }

  showRespawn(seconds) {
    const remaining = Math.max(0, Number(seconds) || 0);
    this.respawnNotice.style.display = remaining > 0 ? 'flex' : 'none';
    if (remaining > 0) this.respawnCountdown.textContent = formatNumber(Math.ceil(remaining));
  }

  showHit() {
    this.hitmarker.style.opacity = '1';
    window.clearTimeout(this.hitTimer);
    this.hitTimer = window.setTimeout(() => {
      this.hitmarker.style.opacity = '0';
    }, 115);
  }

  showDamage() {
    this.damageVignette.classList.add('active');
    window.clearTimeout(this.damageTimer);
    this.damageTimer = window.setTimeout(() => {
      this.damageVignette.classList.remove('active');
    }, 260);
  }
}

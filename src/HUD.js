const persianDigits = new Intl.NumberFormat('fa-IR', { maximumFractionDigits: 0, useGrouping: false });
const formatNumber = (value) => persianDigits.format(Math.max(0, Math.floor(value || 0)));

export class HUD {
  constructor() {
    this.healthFill = document.getElementById('health-fill');
    this.healthValue = document.getElementById('health-value');
    this.healthPanel = document.getElementById('bottom-left');
    this.ammoEl = document.getElementById('ammo');
    this.weaponEl = document.getElementById('weapon-name');
    this.scoreEl = document.getElementById('score');
    this.modeEl = document.getElementById('mode-label');
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
    this.modeEl.textContent = isZombie ? 'بقا · آفلاین' : 'تمرینی · آفلاین';
    this.wavePanel.style.display = isZombie ? 'grid' : 'none';
    if (isZombie) {
      this.waveValue.textContent = formatNumber(stats.wave);
      this.waveHint.textContent = stats.waveIntermission > 0
        ? `موج بعدی تا ${formatNumber(Math.ceil(stats.waveIntermission))} ثانیه`
        : `${formatNumber(stats.remainingCount)} زامبی باقی‌مانده`;
    }
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

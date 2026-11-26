import test from 'node:test';
import assert from 'node:assert/strict';
import { Weapon } from '../src/Weapon.js';

function makeHeadlessWeapon() {
  const weapon = Object.create(Weapon.prototype);
  weapon.weapons = [
    { id: 'rifle', ammo: 2, mag: 30, cooldown: 2, reloading: true, reloadTimer: null },
    { id: 'pistol', ammo: 1, mag: 12, cooldown: 2, reloading: true, reloadTimer: null },
    { id: 'shotgun', ammo: 0, mag: 6, cooldown: 2, reloading: true, reloadTimer: null },
  ];
  weapon.index = 0;
  weapon.triggerDown = true;
  weapon.firedThisPress = true;
  weapon.buildViewModel = () => {};
  return weapon;
}

test('reset applies a saved starter weapon and restores every weapon state', () => {
  const weapon = makeHeadlessWeapon();
  weapon.reset('shotgun');
  assert.equal(weapon.index, 2);
  assert.equal(weapon.weapons[2].ammo, 6);
  assert.equal(weapon.weapons[2].cooldown, 0);
  assert.equal(weapon.weapons[2].reloading, false);
  assert.equal(weapon.triggerDown, false);
  assert.equal(weapon.firedThisPress, false);
});

test('reset safely falls back to the rifle for an unknown saved weapon id', () => {
  const weapon = makeHeadlessWeapon();
  weapon.reset('prototype-only');
  assert.equal(weapon.index, 0);
});

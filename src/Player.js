import * as THREE from 'three';
import { resolveCircleBoxes, clamp } from './collision.js';

// First-person controller with Quake-style movement. Ground acceleration,
// friction and air control are intentionally kept small and easy to tune.
export class Player {
  constructor(camera, colliders, spawn) {
    this.camera = camera;
    this.colliders = colliders;
    this.radius = 0.5;
    this.eyeHeight = 1.7;

    this.groundSpeed = 9.0;
    this.groundAccel = 90.0;
    this.airAccel = 14.0;
    this.friction = 9.0;
    this.stopSpeed = 2.5;
    this.gravity = 22.0;
    this.jumpSpeed = 8.2;

    this.vel = new THREE.Vector3();
    this.onGround = true;
    this.health = 100;
    this.maxHealth = 100;
    this.alive = true;
    this.onDeath = null;
    this.onDamage = null;

    camera.position.copy(spawn);
    camera.position.y = this.eyeHeight;
  }

  reset(spawn) {
    this.camera.position.copy(spawn);
    this.camera.position.y = this.eyeHeight;
    this.vel.set(0, 0, 0);
    this.health = this.maxHealth;
    this.alive = true;
  }

  damage(amount) {
    if (!this.alive || amount <= 0) return;
    const oldHealth = this.health;
    this.health = Math.max(0, this.health - amount);
    if (this.health < oldHealth && this.onDamage) this.onDamage(amount);
    if (this.health <= 0) {
      this.alive = false;
      if (this.onDeath) this.onDeath();
    }
  }

  update(dt, input, bounds) {
    if (!this.alive) return;

    // Build movement directions from the camera, ignoring its pitch.
    const forward = new THREE.Vector3();
    this.camera.getWorldDirection(forward);
    forward.y = 0;
    if (forward.lengthSq() < 1e-6) forward.set(0, 0, -1);
    forward.normalize();
    const right = new THREE.Vector3()
      .crossVectors(forward, new THREE.Vector3(0, 1, 0))
      .normalize();

    // Keyboard values and the virtual joystick share the same movement path.
    const ix = (input.right ? 1 : 0) - (input.left ? 1 : 0) + (input.moveX || 0);
    const iz = (input.forward ? 1 : 0) - (input.back ? 1 : 0) + (input.moveY || 0);
    const wish = new THREE.Vector3();
    wish.addScaledVector(forward, iz);
    wish.addScaledVector(right, ix);

    let wishSpeed = 0;
    if (wish.lengthSq() > 1e-6) {
      wishSpeed = this.groundSpeed * Math.min(1, wish.length());
      wish.normalize();
    }

    // Vertical motion: gravity and a grounded jump.
    this.vel.y -= this.gravity * dt;
    if (input.jump && this.onGround) {
      this.vel.y = this.jumpSpeed;
      this.onGround = false;
    }

    // Ground friction gives the player a quick stop without flattening air movement.
    const speed = Math.hypot(this.vel.x, this.vel.z);
    if (this.onGround && speed > 0) {
      const control = Math.max(speed, this.stopSpeed);
      const drop = control * this.friction * dt;
      const scale = Math.max(speed - drop, 0) / speed;
      this.vel.x *= scale;
      this.vel.z *= scale;
    }

    // Accelerate toward the chosen direction while preserving some air control.
    const accel = this.onGround ? this.groundAccel : this.airAccel;
    if (wishSpeed > 0) {
      const current = this.vel.x * wish.x + this.vel.z * wish.z;
      const add = wishSpeed - current;
      if (add > 0) {
        const amount = Math.min(accel * dt * wishSpeed, add);
        this.vel.x += amount * wish.x;
        this.vel.z += amount * wish.z;
      }
    }

    // Resolve horizontal collisions so the player slides along arena cover.
    let nx = this.camera.position.x + this.vel.x * dt;
    let nz = this.camera.position.z + this.vel.z * dt;
    [nx, nz] = resolveCircleBoxes(nx, nz, this.radius, this.colliders);
    nx = clamp(nx, -bounds + this.radius, bounds - this.radius);
    nz = clamp(nz, -bounds + this.radius, bounds - this.radius);

    // The arena has one floor plane, so clamp vertical motion to eye height.
    let y = this.camera.position.y + this.vel.y * dt;
    if (y <= this.eyeHeight) {
      y = this.eyeHeight;
      this.vel.y = 0;
      this.onGround = true;
    } else {
      this.onGround = false;
    }

    this.camera.position.set(nx, y, nz);
  }
}

"""Kalibrasi sensor: robot diam dan hasil pengukuran tersedia untuk supervisor."""

import json
import sys

from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())
# Argumen opsional hanya dipakai untuk uji kontak terkontrol oleh supervisor.
test_speed = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0

for name in ("motor_kiri", "motor_kanan"):
    motor = robot.getDevice(name)
    motor.setPosition(float("inf"))
    motor.setVelocity(test_speed)

sensors = {}
for name in ("sensor_kiri", "sensor_depan", "sensor_kanan"):
    sensor = robot.getDevice(name)
    sensor.enable(timestep)
    sensors[name] = sensor

while robot.step(timestep) != -1:
    robot.setCustomData(json.dumps({
        "mode": "sensor_calibration",
        "time": robot.getTime(),
        "distances_m": {name: sensor.getValue() for name, sensor in sensors.items()},
    }))

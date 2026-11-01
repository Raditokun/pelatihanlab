from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())


nama_sensor = [
    'sensor_kanan',
    'sensor_kiri',
    'sensor_depan'
]

sensor_us = []
for nama in nama_sensor:
    s = robot.getDevice(nama)
    s.enable(timestep)
    sensor_us.append(s)
    
motor_kiri = robot.getDevice('motor_kiri')
motor_kanan = robot.getDevice('motor_kanan')

motor_kiri.setPosition(float('inf'))
motor_kanan.setPosition(float('inf'))

motor_kiri.setVelocity(2.0)
motor_kanan.setVelocity(2.0)

while robot.step(timestep) != -1:
    kanan = sensor_us[0].getValue()
    kiri = sensor_us[1].getValue()
    depan = sensor_us[2].getValue()

    print(
        f"Kiri: {kiri:.2f} | "
        f"Depan: {depan:.2f} | "
        f"Kanan: {kanan:.2f}"
    )
    
    
    
 #if depan < 900.00, cek kanan 
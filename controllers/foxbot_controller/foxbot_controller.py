from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())


nama_sensor = [
    'sensor_kanan',
    'sensor_depan_kananujung',
    'sensor_depan_kanan1',
    'sensor_depan_kanan2',
    'sensor_depan_kanan3',
    'sensor_depan_kanan4',
    'sensor_depan',
    'sensor_depan_kiri4',
    'sensor_depan_kiri3',
    'sensor_depan_kiri2',
    'sensor_depan_kiri1',
    'sensor_depan_kiriujung',
    'sensor_kiri'
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

motor_kiri.setVelocity(0.0)
motor_kanan.setVelocity(0.0)

jarak_nabrak = 0.15       
jarak_aman_samping = 0.15 
kecepatan_maju = 4.0     
kecepatan_belok = 3.0    
durasi_belok_90 = 1.23   
belok_sampai = 0.0

while robot.step(timestep) != -1:
    kanan = sensor_us[0].getValue()
    kanan_ujung = sensor_us[1].getValue()

    depan_kanan1 = sensor_us[2].getValue()
    depan_kanan2 = sensor_us[3].getValue()
    depan_kanan3 = sensor_us[4].getValue()
    depan_kanan4 = sensor_us[5].getValue()

    depan_tengah = sensor_us[6].getValue()

    depan_kiri4 = sensor_us[7].getValue()
    depan_kiri3 = sensor_us[8].getValue()
    depan_kiri2 = sensor_us[9].getValue()
    depan_kiri1 = sensor_us[10].getValue()

    kiri_ujung = sensor_us[11].getValue()
    kiri = sensor_us[12].getValue()

 
    depan = min(
        kanan_ujung,
        depan_kanan1,
        depan_kanan2,
        depan_kanan3,
        depan_kanan4,
        depan_tengah,
        depan_kiri4,
        depan_kiri3,
        depan_kiri2,
        depan_kiri1,
        kiri_ujung
    )
    

    print(
        f"Depan={depan:.3f} | "
        f"Pojok kiri={kiri_ujung:.3f} | "
        f"Pojok kanan={kanan_ujung:.3f} | "
    )

    waktu = robot.getTime()
    
    jarak_darurat = 0.05 
    jarak_darurat_samping = 0.08

   
    # Kalau kanan terlalu mepet, belok kiri
    if depan >= jarak_nabrak and kanan < jarak_darurat and kanan < kiri:
        print("KANAN MEPET!")
        motor_kiri.setVelocity(-2.0)
        motor_kanan.setVelocity(6.0)
        continue

   # Kalau kiri terlalu mepet, belok kanan
    elif depan >= jarak_nabrak and kiri < jarak_darurat:
        print("KIRI MEPET!")
        motor_kiri.setVelocity(6.0)
        motor_kanan.setVelocity(-2.0)
        continue

    
    if waktu < belok_sampai:
        continue
        
    

    if depan < jarak_nabrak:
        print("NABRAK LE!")

        if kiri >= jarak_aman_samping and kiri >= kanan:
            print("kiri")
            motor_kiri.setVelocity(-kecepatan_belok)
            motor_kanan.setVelocity(kecepatan_belok)
            belok_sampai = waktu + durasi_belok_90

        elif kanan >= jarak_aman_samping:
            print("kanan.")
            motor_kiri.setVelocity(kecepatan_belok)
            motor_kanan.setVelocity(-kecepatan_belok)
            belok_sampai = waktu + durasi_belok_90

        else:
            print("180")
            motor_kiri.setVelocity(-kecepatan_belok)
            motor_kanan.setVelocity(kecepatan_belok)
            belok_sampai = waktu + 2 * durasi_belok_90

    else:
        motor_kiri.setVelocity(kecepatan_maju)
        motor_kanan.setVelocity(kecepatan_maju)
        
        
    

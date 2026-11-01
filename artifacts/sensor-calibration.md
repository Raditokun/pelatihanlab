# Kalibrasi sensor foxbot

Ketiga sensor tetap bertipe sonar. Jangkauan 0.20 m, nilai keluaran dalam meter, tanpa noise, resolusi 0.001 m.

| Sensor | Arah lokal robot | Posisi lokal (m) |
| --- | --- | --- |
| sensor_depan | +X / depan | 0.158, 0, 0 |
| sensor_kiri | +Y / kiri | 0.13, 0.108, 0 |
| sensor_kanan | -Y / kanan | 0.13, -0.108, 0 |

Sumbu kiri dan kanan mengikuti arah hadap robot, bukan arah layar. Casing sensor berwarna oranye; sisi gelap menghadap arah pengukuran.

Semua lookupTable:

```text
0 0 0
0.2 0.2 0
```

0.050 berarti 5 cm. 0.100 berarti 10 cm. 0.200 berarti batas jangkauan atau tidak ada pantulan valid.

Controller foxbot_controller.py tetap berisi kode pengguna untuk membaca sensor dan maju dengan dua motor. Ditambahkan satuan m pada Console dan konstanta JARAK_WASPADA = 0.10 agar kondisi seperti if depan < JARAK_WASPADA mudah ditulis. Tidak ditambahkan algoritma belok atau obstacle avoidance.

Robot ditempatkan kembali di tengah arena, orientasi +X; simulasi ditinggalkan pause. Controller tambahan foxbot_sensor_check dipakai untuk pengujian; tidak dipasang pada world akhir.

## Hasil pengujian langsung di Webots

| Kasus | Kiri (m) | Depan (m) | Kanan (m) | Hasil |
| --- | --- | --- | --- | --- |
| clear | 0.200 | 0.200 | 0.200 | Lulus |
| front_10cm | 0.200 | 0.100 | 0.200 | Lulus |
| left_10cm | 0.100 | 0.200 | 0.200 | Lulus |
| right_10cm | 0.200 | 0.200 | 0.100 | Lulus |
| all_10cm | 0.100 | 0.100 | 0.100 | Lulus |
| front_5cm | 0.200 | 0.050 | 0.200 | Lulus |
| front_19cm | 0.200 | 0.190 | 0.200 | Lulus |
| front_beyond_range | 0.200 | 0.200 | 0.200 | Lulus |
| front_wall_contact | 0.200 | 0.006 | 0.200 | Lulus |

Pengujian statis memakai objek pada arah depan, kiri, dan kanan dengan permukaan tegak lurus sinar. Batas kesalahan uji 3 mm. Pada uji kontak sambil motor maju 2 rad/s, pembacaan depan 0.006 m dan jarak geometris sekitar 0.00565 m. Casing dimasukkan ke boundingObject Group robot sehingga asal sinar terlindungi saat kontak. Semua objek uji sudah dihapus dari world akhir.

Sonar tetap bergantung pada sudut pantulan: permukaan terlalu miring bisa menghasilkan nilai maksimum walaupun ada objek. Tiga sinar ini tidak memberikan cakupan 360 derajat. Sensor kiri dan kanan mengukur sisi robot, sehingga tidak harus ikut berubah ketika hanya ada tembok di depan.

Referensi: [DistanceSensor Webots R2025a](https://github.com/cyberbotics/webots/blob/R2025a/docs/reference/distancesensor.md).

Backup sebelum perubahan ada pada artifacts/sensor-fix-backup/. Hasil terstruktur terdapat pada sensor-calibration-results.json; ilustrasi uji terdapat pada foxbot-sensor-calibration.png.

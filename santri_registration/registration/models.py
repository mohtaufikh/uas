from django.db import models

class Santri(models.Model):
    ASRAMA_CHOICES = [
        ('A', 'Asrama A'),
        ('B', 'Asrama B'),
        ('C', 'Asrama C'),
    ]

    KAMAR_CHOICES = [
        ('A1', 'Kamar A1'), ('A2', 'Kamar A2'), ('A3', 'Kamar A3'), ('A4', 'Kamar A4'), ('A5', 'Kamar A5'),
        ('B1', 'Kamar B1'), ('B2', 'Kamar B2'), ('B3', 'Kamar B3'), ('B4', 'Kamar B4'), ('B5', 'Kamar B5'),
        ('C1', 'Kamar C1'), ('C2', 'Kamar C2'), ('C3', 'Kamar C3'), ('C4', 'Kamar C4'), ('C5', 'Kamar C5'),
    ]

    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    orangtua_wali = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)
    riwayat_pendidikan = models.TextField()
    asal_sekolah = models.CharField(max_length=100)
    tanggal_masuk = models.DateField()
    asrama = models.CharField(max_length=1, choices=ASRAMA_CHOICES)
    kamar = models.CharField(max_length=2, choices=KAMAR_CHOICES)

    def __str__(self):
        return self.nama


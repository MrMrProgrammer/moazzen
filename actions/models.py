from django.db import models
from users.models import Users

PRAYER_CHOICES = [
    ('fajr', 'نماز صبح'),
    ('dhuhr', 'نماز ظهر'),
    ('asr', 'نماز عصر'),
    ('maghrib', 'نماز مغرب'),
    ('isha', 'نماز عشا'),
]

TYPE_CHOICES = [
    ('main', 'اصلی'),
    ('backup', 'ذخیره'),
]


class Azan(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="کاربر"
    )
    date = models.DateField(
        verbose_name="تاریخ"
    )
    prayer = models.CharField(
        max_length=20,
        choices=PRAYER_CHOICES,
        verbose_name="نماز"
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name="نوع"
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name="تایید شده؟"
    )

    class Meta:
        db_table = "azans"
        verbose_name = "اذان"
        verbose_name_plural = "اذان ها"

    def __str__(self):
        prayer_name = dict(PRAYER_CHOICES).get(self.prayer, self.prayer)
        return f"{self.user} - {prayer_name} - {self.date}"


class Takbeer(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="کاربر"
    )
    date = models.DateField(
        verbose_name="تاریخ"
    )
    prayer = models.CharField(
        max_length=20,
        choices=PRAYER_CHOICES,
        verbose_name="نماز"
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name="نوع"
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name="تایید شده؟"
    )

    class Meta:
        db_table = "takbeers"
        verbose_name = "تکبیر"
        verbose_name_plural = "تکبیر ها"

    def __str__(self):
        prayer_name = dict(PRAYER_CHOICES).get(self.prayer, self.prayer)
        return f"{self.user} - {prayer_name} - {self.date}"

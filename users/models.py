from django.db import models
from django.contrib.auth.hashers import make_password, check_password

from utils.date_time import date_to_shamsi


class Users(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="نام"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="نام خانوادگی"
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="تاریخ تولد"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="تلفن همراه"
    )
    profile = models.ImageField(
        upload_to="media/profiles",
        verbose_name="پروفایل"
    )
    otp = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="رمز یکبار مصرف"
    )
    expires_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="زمان انقضاء"
    )
    password = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="رمز عبور"
    )

    class Meta:
        db_table = "users"
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def date_of_birth_shamsi(self):
        return date_to_shamsi(self.date_of_birth)
    date_of_birth_shamsi.short_description = "تاریخ تولد"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    full_name.short_description = "نام و نام خانوادگی"

    def has_profile(self):
        if self.profile:
            return True
        else:
            return False        
    has_profile.short_description = "پروفایل دارد؟"

    def set_password(self, raw_password):
        """هش کردن رمز عبور و ذخیره آن."""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """بررسی رمز عبور."""
        return check_password(raw_password, self.password)

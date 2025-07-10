from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.date_time import date_to_shamsi


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        # verbose_name="تاریخ تولد"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        # verbose_name="تلفن همراه"
    )
    profile = models.ImageField(
        upload_to="media/profiles",
        blank=True,
        null=True,
        # verbose_name="پروفایل"
    )
    otp = models.IntegerField(
        blank=True,
        null=True,
        # verbose_name="رمز یکبار مصرف"
    )
    otp_expires_at = models.DateTimeField(
        blank=True,
        null=True,
        # verbose_name="زمان انقضاء"
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username"]
    
    class Meta:
        db_table = "custom_user"
        # verbose_name = "کاربر"
        # verbose_name_plural = "کاربران"
    
    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username
    
    def date_of_birth_shamsi(self):
        return date_to_shamsi(self.date_of_birth)
    date_of_birth_shamsi.short_description = "تاریخ تولد"

    def has_profile(self):
        if self.profile:
            return True
        else:
            return False        
    has_profile.short_description = "پروفایل دارد؟"

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ('man', "Мужчина"),
        ('woman', "Женщина")
    ]
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар')
    user_information = models.TextField(null=True, blank=True, verbose_name='Информация о пользователе')
    phone_number = models.CharField(max_length=16, null=True, blank=True, verbose_name='Номер телефона')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='пол')
    publication_counter = models.PositiveIntegerField(default=0, verbose_name='Счетчик публикации')
    subscription_counter = models.PositiveIntegerField(default=0, verbose_name='Счетчик подписок')
    subscriber_counter = models.PositiveIntegerField(default=0, verbose_name='Счетчик подписчиков')

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель для пользователей"""

    username = models.CharField("Уникальный юзернейм", max_length=150, unique=True)
    password = models.CharField(
        "Пароль",
        max_length=150,
    )
    email = models.EmailField(
        "Адрес электронной почты",
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(
        "Имя",
        max_length=150,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=150,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username} {self.first_name}"


class Follow(models.Model):
    """Модель для подписчиков"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Автор",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "author"], name="Вы уже подписаны на данного автора"
            ),
        ]
        ordering = ["-id"]
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def str(self):
        return f"{self.user} подписался на {self.author}"

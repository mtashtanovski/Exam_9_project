from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Picture(models.Model):
    image = models.ImageField(
        verbose_name="Фото",
        upload_to="media/",
        null=False,
        blank=False,
    )
    signature = models.TextField(
        max_length=200,
        verbose_name="Подпись",
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    author = models.ForeignKey(
        User,
        related_name="pictures",
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Автор",
        null=False,
    )
    album = models.ForeignKey(
        'webapp.Album',
        on_delete=models.CASCADE,
        related_name='pictures',
        verbose_name="Альбом",
        null=True,
        blank=True,
    )
    is_private = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Приватный",
    )

    def __str__(self):
        return f"{self.image} {self.signature}"

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Album(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        verbose_name="Название"
    )
    description = models.TextField(
        max_length=300,
        verbose_name="Описание",
    )
    author = models.ForeignKey(
        User,
        related_name="albums",
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Автор",
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    is_private = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Приватный"
    )

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        permissions = (
            ('add_picture_in_own_album', "Добавлять фото в свой альбом"),
            ('change_picture_in_own_album', "Удалять фото из своего альбома"),
        )

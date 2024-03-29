from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Publication(models.Model):
    picture = models.ImageField(upload_to='publication/picture/', verbose_name='Аватар')
    descriptions = models.TextField(verbose_name='Описание')
    likes_count = models.PositiveIntegerField(default=0, verbose_name='Счетчик лайков')
    comments_count = models.PositiveIntegerField(default=0, verbose_name='Счетчик комментариев')
    author = models.ForeignKey(get_user_model(), related_name='publications', on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    users_like = models.ManyToManyField(get_user_model())

    def __str__(self):
        return f'{self.descriptions} {self.created}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.author.publication_counter += 1
            self.author.save()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.author.publication_counter -=1
        self.author.save()
        return super().delete(*args, **kwargs)

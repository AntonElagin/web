from django.db import models
from django.contrib.auth.models import User


class Creator(models.Model):
    profile_image = models.ImageField(null=True, blank=True, verbose_name='Profile image')
    name = models.CharField(max_length=255, verbose_name='Name of User')
    bio = models.TextField(null=True, blank=True, verbose_name='Bio')
    website = models.CharField(max_length=200, null=True, blank=True, verbose_name='Website')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Creator'
        verbose_name_plural = 'Creators'


class Follow(models.Model):
    author = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='author')
    follower = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='follower')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} follows {}'.format(self.follower, self.author)

    class Meta:
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'

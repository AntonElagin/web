from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, AbstractBaseUser, PermissionsMixin


class Creator(AbstractBaseUser, PermissionsMixin):
    profile_image = models.ImageField(null=True, blank=True, verbose_name='Profile image')
    name = models.CharField(max_length=255, verbose_name='Name of User')
    bio = models.TextField(null=True, blank=True, verbose_name='Bio')
    website = models.CharField(max_length=255, null=True, blank=True, verbose_name='Website')
    username = models.CharField(max_length=50, null=False, unique=True)
    # email = models.EmailField(max_length=255, null=False, verbose_name='Email', unique=True)
    # password = models.CharField(max_length=100, null=False, verbose_name='Password')

    USERNAME_FIELD = "username"

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.username


class Follow(models.Model):
    author = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='Author')
    follower = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='Follower')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{follower} follows {idol}'.format(follower=self.follower, idol=self.author)

    class Meta:
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'

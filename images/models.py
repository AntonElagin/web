from django.db import models
from users.models import Creator


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Image(models.Model):
    file = models.ImageField(verbose_name='File')
    location = models.CharField(max_length=140, verbose_name='Location')
    caption = models.TextField(verbose_name='Caption')
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return 'Image #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Comment(models.Model):
    message = models.TextField(verbose_name='Message')
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Comment #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Like(models.Model):
    user = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Like #{}'.format(self.pk)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

from django.db import models
from users.models import Creator
# from location_field.models.spatial import LocationField


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Image(models.Model):
    file = models.ImageField(verbose_name='File')
    location = models.CharField(max_length=100, verbose_name='Location')
    # city = models.CharField(max_length=255)
    # location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    caption = models.TextField(verbose_name='Caption')
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Comment(models.Model):
    message = models.TextField(verbose_name='Message')
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Like(models.Model):
    user = models.ForeignKey(Creator, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

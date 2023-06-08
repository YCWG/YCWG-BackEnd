from django.db import models


class Party(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='', blank=True, null=True)
    category = models.CharField(max_length=24)
    place = models.CharField(max_length=255)
    member_limit = models.IntegerField()
    now_member = models.IntegerField(default = 1)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    upload_date = models.DateTimeField('UPLOAD DATE', auto_now_add=True)

    class Meta:
        ordering = ('upload_date',)

    def __str__(self):
        return self.title
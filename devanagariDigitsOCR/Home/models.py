from django.db import models
from django.urls import reverse


class OCRimage(models.Model):
    imgFile = models.ImageField(blank=False)

    def __str__(self):
        return "{}".format(self.imgFile)


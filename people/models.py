from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=32, verbose_name='名字')
    age = models.IntegerField(verbose_name='年龄')

    class Meta:
        verbose_name = "人员表"

    def __repr__(self):
        return self.name

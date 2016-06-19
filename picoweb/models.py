from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=20)
    usedmodel = models.CharField(max_length=20)
    features = models.TextField(default='')
    watt_normal = models.IntegerField()
    watt_peak = models.IntegerField()
    vin_min = models.IntegerField()
    vin_max = models.IntegerField()
    pcb_length_mm = models.FloatField()
    pcb_width_mm = models.FloatField()
    pcb_height_mm = models.FloatField()
    input_connector = models.CharField(max_length=50)
    price_usd = models.FloatField()
    discount_off_percent = models.FloatField()

    class meta:
        ordering = ['model']

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=100)
    size = models.CharField(max_length=100, default='750x500')
    image = models.ImageField(upload_to='photos')

    class meta:
        ordering = ["title"]

    def __unicode__(self):
        return self.title


class Download(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='downloads')

    class meta:
        ordering = ["title"]

    def __unicode__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

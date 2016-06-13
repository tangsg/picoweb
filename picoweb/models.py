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
    	pcb_length = models.FloatField()
    	pcb_width = models.FloatField()
    	pcb_height = models.FloatField()
    	input_connector = models.CharField(max_length=50)

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

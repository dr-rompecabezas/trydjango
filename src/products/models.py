from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
	# Map to database using TextField method
	title 		= models.CharField(max_length=120) # max_length = required
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=10000)
	summary 	= models.TextField(blank=False, null=False)
	featured	= models.BooleanField(default=False)

	# in case urls change; see product_list.html template for an example
	def get_absolute_url(self):
		return reverse("products:product-lookup", kwargs={"id": self.id})
	
	# def get_absolute_url(self):
	# 	return f"/products/{self.id}/"

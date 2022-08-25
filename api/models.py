from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
	mark = models.CharField(verbose_name="Марка", max_length=100)
	model = models.CharField(verbose_name="Модель", max_length=100)
	broken = models.BooleanField(verbose_name="Битая", default=False)
	power = models.IntegerField(verbose_name="Мощность")
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey("auth.User", 
                           on_delete=models.CASCADE, 
                           related_name="cars")

	class Meta:
		db_table = "Машина"
		ordering = ['created']

	def save(self, *args, **kwargs):
		super(Car, self).save(*args, **kwargs)

	def __str__(self) -> str:
		return (self.mark)

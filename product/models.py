from django.db import models

# Create your models here.
class product(models.Model):
    ProdName =models.CharField(max_length=50) 
    ProdDesc= models.TextField(max_length=1000)
    ProdPrice = models.DecimalField(max_digits=5,decimal_places=2)
    ProdCost = models.DecimalField(max_digits=5,decimal_places=2)
    ProdCreated = models.DateTimeField(auto_now= False)
    ProdImage = models.ImageField(upload_to='product/', blank=True , null =True)


    def __str__ (self):
        return self.ProdName

 

class ProductImage(models.Model):
    Prdproduct= models.ForeignKey(product, on_delete=models.CASCADE)
    ProdImage = models.ImageField(upload_to='product/', blank=True , null =True)



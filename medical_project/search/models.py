from django.db import models

# Create your models here.
class Medicine(models.Model):

    product_id = models.IntegerField( null=True)
    sku_name = models.CharField( max_length=255)
    price = models.FloatField()
    manufacturer_name = models.CharField( max_length=255)
    salt_name = models.CharField(max_length=255)
    drug_form = models.CharField(max_length=150)
    pack_size = models.CharField(max_length=150)
    strength = models.CharField(max_length=50)
    product_banned_flag = models.BooleanField( null=True)
    unit = models.CharField(max_length=50, null=True)
    price_per_unit = models.FloatField(null=True)

    def __str__(self):
        return self.sku_name
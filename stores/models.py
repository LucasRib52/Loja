from django.db import models

#aqui criamos a tabela pro banco de dados

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=300, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='store_brand')
    value = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=800)
    photo = models.ImageField(upload_to='stores/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.item
    

class StoreInventory(models.Model):
    stores_count = models.IntegerField()
    stores_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.stores_count} - {self.stores_value}'
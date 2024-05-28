from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from stores.models import Store, StoreInventory


def store_inventory_update():
    stores_count = Store.objects.all().count()
    stores_value = Store.objects.aggregate(
        total_value=Sum('value')
    )['total_value'] or 0 # Garante que stores_value seja 0 se for None
    StoreInventory.objects.create(
        stores_count=stores_count,
        stores_value=stores_value
    )

@receiver(pre_save, sender=Store)
def store_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada Automaticamente'

@receiver(post_save, sender=Store)
def store_post_save(sender, instance, **kwargs):
     store_inventory_update()

@receiver(post_delete, sender=Store)
def store_post_delete(sender, instance, **kwargs):
    store_inventory_update()

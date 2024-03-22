from django.db import models


class ItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    objects = ItemManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Сортировка по полю 'order'

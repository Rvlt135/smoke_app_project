from django.db import models
import uuid


class Strain(models.Model):
    objects = None
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('CategoryStrain', on_delete=models.PROTECT, null=True)
    flavors = models.ForeignKey('CountersByFlavors', on_delete=models.PROTECT, null=True)
    # reviewsCountByEffects = models.ForeignKey('CountersByEffect', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class CategoryStrain(models.Model):
    category = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.category


class CountersByEffect(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    type = models.CharField(max_length=100, db_index=True)
    # counters = models.IntegerField()

    def __str__(self):
        return self.name


class CountersByFlavors(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

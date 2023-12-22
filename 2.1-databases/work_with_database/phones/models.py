from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True)
    image = models.URLField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        db_table = 'phone_table'

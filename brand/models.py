from django.db import models
from django.urls import reverse

# Create your models here.
class brand(models.Model):
    brand_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    brand_image = models.ImageField(upload_to="photos/products", default="")
    is_delete=models.BooleanField(default=True)
    def get_url_brand(self):
        return reverse('market_by_brand',args=[self.slug])

    def __str__(self):
        return str(self.brand_name)

    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"


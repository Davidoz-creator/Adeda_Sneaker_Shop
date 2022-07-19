from enum import unique
from django.db import models
from accounts.models import Profile
from autoslug import AutoSlugField
from videoprops import get_video_properties

# Create your models here.
class Destiny(models.Model):
    brand=models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=15,
    )
    size=models.IntegerField(
        null=False,
        blank=False,
        
    )
    name=models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=15,
    )
    

class Product(models.Model):
    # store = models.ForeignKey("store.Store", null=True, on_delete=models.SET_NULL, related_name='product_store')
    # category = models.ForeignKey("store.Category", related_name='product_category', on_delete=models.CASCADE)
    # sub_category = models.ForeignKey("store.SubCategory", related_name='product_sub_category', on_delete=models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    # product_condition = models.ForeignKey(ProductCondition, null=True, on_delete=models.SET_NULL, related_name='product_condition')    
    slug = AutoSlugField(populate_from='title',unique=True,)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    weight = models.FloatField()
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    admin_restricted = models.BooleanField(default=False)
    image_added = models.BooleanField(default=False)
    delete_product = models.BooleanField(default=False)

    main_video = models.FileField(max_length=255, upload_to="images", null=True, blank=True)
    main_image = models.ImageField(max_length=255, upload_to="images", null=True, blank=True)
    main_image_thumbnail = models.ImageField(max_length=255, upload_to="images", null=True, blank=True)
    main_image_small_thumbnail = models.ImageField(max_length=255, upload_to="images", null=True, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

  



    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-date_created',)

    # This code must always return id. It enables me get the first object in cart ID.
    def __str__(self):
        return str(self.id)  
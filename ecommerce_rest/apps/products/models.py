from django.db import models
from base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.
class MeasureUnit(BaseModel):
    description = models.CharField('Description', max_length=255, null=True, blank=True, unique=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Measure Unit'
        verbose_name_plural = 'Measure Units'
    
    def __str__(self):
        return self.description
    
class CategoryProduct(BaseModel):
    description = models.CharField('Description', max_length=255, null=True, blank=True, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, null=True, blank=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Category Product'
        verbose_name_plural = 'Category Products'
    
    def __str__(self):
        return self.description

class Indicator(BaseModel):

    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True, blank=True)
    discount_value = models.PositiveSmallIntegerField('Discount Value', default=0)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'
    
    def __str__(self):
        return f"{self.category_product} - {self.discount_value}%"

class Product(BaseModel):
    name = models.CharField('Name', max_length=255, null=True, blank=True)
    description = models.TextField('Description', null=False, blank=False)
    image = models.ImageField('Image', upload_to='products/', null=True, blank=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True, blank=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
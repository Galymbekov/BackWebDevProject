from django.db import models

class Shop(models.Model):
    like = models.BooleanField(default=False)
    price = models.FloatField(max_length=200, default=None)
    description = models.CharField(max_length=200, default=None)

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def to_json(self):
        return {
            'like': self.like,
            'price': self.price,
            'description': self.description
        }

class Filter(models.Model):
    fromdata = models.FloatField(max_length=200, default=None)
    enddata = models.FloatField(max_length=200, default=None)

    class Meta:
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'

    def to_json(self):
        return {
            'fromdata': self.fromdata,
            'enddata': self.enddata
        }

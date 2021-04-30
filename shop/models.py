from django.db import models


class Shop(models.Model):
    id = models.IntegerField(primary_key=True)
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


class Whishlist(models.Model):
    ids = models.ForeignKey(Shop, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Liked'

    def to_json(self):
        return {
            'ids': self.ids,
            'liked': self.liked
        }

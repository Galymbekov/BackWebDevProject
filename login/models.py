from django.db import models
from registration.models import Registration


class Manager(models.Manager):
    people = models.Manager()

    def to_json(self):
        return {
            'people': self.people
        }


class Login(models.Model):
    id = models.ForeignKey(Registration.id, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, default=None)
    password = models.CharField(max_length=200, default=None)
    remember = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Logins'

    def to_json(self):
        return {
            'username': self.username,
            'password': self.password,
            'remember': self.remember
        }

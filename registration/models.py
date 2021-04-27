from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=200, default=None)
    email = models.EmailField(max_length=200, default=None)
    username = models.CharField(max_length=200, default=None)
    password = models.CharField(max_length=200, default=None)
    confpass = models.CharField(max_length=200, default=None)

    class Meta:
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'

    def to_json(self):
        return {
            'name': self.name,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'confpass': self.confpass
        }

from django.db import models

class Login(models.Model):
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

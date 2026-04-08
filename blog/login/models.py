from django.db import models

#  роли пользователей
class Role(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

# пользователь
class User(models.Model):
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    balance = models.FloatField(default=0.0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
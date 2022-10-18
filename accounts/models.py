from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    python_skill = models.IntegerField(default=0)
    sql_skill = models.IntegerField(default=0)
    java_skill = models.IntegerField(default=0)
    spark_skill = models.IntegerField(default=0)
    html_css_skill = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

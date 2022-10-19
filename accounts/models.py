import hashlib
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

    @property
    def employeeUsername(self):
        return self.user.username

    def avatarMd5(self):
        return("https://www.gravatar.com/avatar/" + str(hashlib.md5(self.user.username.encode()).hexdigest()))

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  resume = models.FileField(upload_to='resume/', null=True, blank=True)
  profile_picture = models.ImageField(upload_to='images/profile-pictures/', null=True, blank=True)
  primary_text = models.TextField(max_length=1000, null=True, blank=True)

  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}'

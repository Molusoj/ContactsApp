from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    other_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(blank=True, max_length=20)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
        ('undisclosed', 'Undisclosed')
    ), default='Undisclosed')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

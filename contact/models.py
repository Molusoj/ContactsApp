from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.


class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='contact-image/default.jpg', upload_to="contact-image")
    name = models.CharField(max_length=150)
    phone_number = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
        ('undisclosed', 'Undisclosed')
    ), default='Undisclosed')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

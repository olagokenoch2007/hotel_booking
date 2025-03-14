from django.db import models

# Create your models here.
class Apartment (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price per night")
    beds = models.PositiveIntegerField(verbose_name="Number of beds")
    baths = models.PositiveIntegerField(verbose_name="Number of baths")
    wifi_available = models.BooleanField(default=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)
    image = models.FileField(upload_to='rooms/')
    available = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Staff(models.Model):
    image = models.FileField(upload_to='uploads/', null=True, blank=True, verbose_name='Profile Picture')
    name = models.CharField(max_length= 100)
    role = models.CharField(max_length= 30)
    bio = models.TextField(null=True, blank= True)
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length= 200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class Booking(models.Model):
    name = models.CharField(max_length= 255)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    adult = models.PositiveIntegerField()
    child = models.PositiveIntegerField(blank=True, null = True)
    room = models.ForeignKey(Apartment, on_delete=models.CASCADE, default=1)
    special_request = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

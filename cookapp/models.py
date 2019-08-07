from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# class Ingredient(models.Model):
#     code = models.IntegerField(null=True)
#     name = models.CharField(max_length=10, null=True)
#     category = models.CharField(max_length = 10, null=True)
#     def __str__(self):
#         return self.name

# class Recipe(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     url = models.URLField(null=True)
#     image = models.ImageField(upload_to='images/', null=True, blank=True)
#     ingredients = models.ManyToManyField(Ingredient)
#     image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(480,240)])

#     def __str__(self):
#         return self.name

class Category(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length = 10)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='images/', blank=True)
    ingredients = models.ManyToManyField(
        Ingredient
    )
    image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(480,240)])

    def __str__(self):
        return self.name

    def convert_youtube(self):
        return "https://www.youtube.com/embed/"+self.url.split('/')[-1].split('=')[-1]

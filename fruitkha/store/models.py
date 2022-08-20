from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='thumbnail', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

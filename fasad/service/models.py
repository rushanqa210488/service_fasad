from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField(null=True, blank=True )
    price  = models.IntegerField(null=True, blank=True) 
    image = models.ImageField(upload_to="image", verbose_name="Фото")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='service')


    def __str__(self) -> str:
        return self.title
    

class Photo(models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(verbose_name='Фотографий', upload_to='photo')
    

from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    #adding new field terus nanti di makemigration again
    author = models.CharField(null= True, max_length=100)
    is_bestselling = models.BooleanField(default= False)
    slug = models.SlugField(_(""))

    ### method di bawah ini kita coba ovverideding si methodnya 
    # untuk manggil page yang akan kitabuat ###

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"
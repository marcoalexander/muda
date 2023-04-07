from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    CATEGORIES = (
        ('DRESSY', 'Dressy'),
        ('DRESSY_CAUSAL', 'Dressy Casual'),
        ('STREETWARE', 'Streetware'),
    )
    category = models.CharField(max_length=25, choices=CATEGORIES)
    # category = ListCharField(
    #    base_field = models.CharField(max_length=25, choices=CATEGORIES),
    #    size=5,
    #    max_length=(5*26)
    #)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts_something')
    
    object = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title


# Create your models here.

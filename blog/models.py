from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tags(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name_plural = "Tags"

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="", blank=True, null=False,db_index=True,unique=True)
    content = models.CharField(max_length=20000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null = True)
    tags = models.ManyToManyField(Tags)
    excerpt = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title}"

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

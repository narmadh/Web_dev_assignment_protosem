from django.db import models


# Create your models here.
class PostTable(models.Model):
    # post_id
    title = models.CharField(max_length=200)
    description = models.TextField()
    publisher_time = models.DateTimeField(auto_now_add=True)
    # author
    # blog_image = models.ImageField()

    def __str__(self):
        return self.title

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='categories/icons/', blank=True, null=True)
    image = models.ImageField(upload_to='categories/images/', blank=True, null=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=500)
    options = models.JSONField(default=list)
    correct_index = models.IntegerField()

    def __str__(self):
        return self.text

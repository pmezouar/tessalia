from django.db import models

# Create your models here.
class Category(models.Model):
    image = models.FileField(upload_to="public/categories/")
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name}"
    
class Symptom(models.Model):
    icon = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"
    
class Care(models.Model):
    icon = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name}"
    
class Pathology(models.Model):
    image = models.FileField(upload_to="public/pathologies/")
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    severity = models.CharField(max_length=150)
    prevalence = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="pathologies")
    symptoms = models.ManyToManyField(Symptom, blank=True, related_name="pathologies")
    cares = models.ManyToManyField(Care, blank=True, related_name="pathologies")

    def __str__(self):
        return f"{self.name}"
    
class Resource(models.Model):
    image = models.FileField(upload_to="public/ressources/")
    file = models.FileField(upload_to="public/ressources/")
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description_short = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name}"
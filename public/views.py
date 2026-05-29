from django.shortcuts import render
from django import forms

from .models import Category, Symptom, Care, Pathology, Resource

class SearchForm(forms.Form):
    search = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Rechercher..."
        })
    )

# Create your views here.
def index(request):
    categories = Category.objects.all().order_by("name")
    
    return render(request, "public/index.html", {
        "searchForm" : SearchForm(),
        "categories": categories
        
    })
    
def categories(request):
    categories = Category.objects.all().order_by("name")
    
    return render(request, "public/categories.html", {
        "searchForm" : SearchForm(),
        "categories": categories
    })
    
def category(request, category_slug):
    category = Category.objects.filter(slug=category_slug).first()
    pathologies = Pathology.objects.filter(category=category).all().order_by("name")
    
    return render(request, "public/category.html", {
        "searchForm" : SearchForm(),
        "category": category,
        "pathologies": pathologies
    })
    
def pathologies(request):
    pathologies = Pathology.objects.all().order_by("name")
    
    return render(request, "public/pathologies.html", {
        "searchForm" : SearchForm(),
        "pathologies": pathologies
    })
    
def pathology(request, pathology_slug):
    pathology = Pathology.objects.filter(slug=pathology_slug).first()
    symptoms = pathology.symptoms.all()
    cares = pathology.cares.all()
    
    return render(request, "public/pathology.html", {
        "searchForm" : SearchForm(),
        "pathology": pathology,
        "symptoms": symptoms,
        "cares": cares        
    })

def search(request):
    query = request.GET.get("search")

    results = []

    if query:
        results = Pathology.objects.filter(name__icontains=query)

    return render(request, "public/search.html", {
        "searchForm" : SearchForm(),
        "query": query,
        "results": results
    })
    
def resources(request):
    resources = Resource.objects.all().order_by("name")
    
    return render(request, "public/resources.html", {
        "searchForm" : SearchForm(),
        "resources": resources
    })
    
def resource(request, resource_slug):
    resource = Resource.objects.filter(slug=resource_slug).first()
    
    return render(request, "public/resource.html", {
        "searchForm" : SearchForm(),
        "resource": resource     
    })
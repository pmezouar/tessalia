from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.categories, name="categories"),
    path("categorie/<str:category_slug>", views.category, name="category"),
    path("pathologies/", views.pathologies, name="pathologies"),
    path("pathologie/<str:pathology_slug>", views.pathology, name="pathology"),
    path("recherche/", views.search, name="search"),
    path("ressources/", views.resources, name="resources"),
    path("ressource/<str:resource_slug>", views.resource, name="resource"),
]


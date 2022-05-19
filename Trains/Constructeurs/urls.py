from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add),
    path("traitement/", views.traitement),
    path("", views.index),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>", views.updatetraitement),
    path("delete/<int:id>/", views.delete),
]
from django.urls import path
from . import views
from . import Constructeurs_views

urlpatterns = [
# Locomotives
    path("add/", views.add),
    path("traitement/", views.traitement),
    path("index", views.index),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>", views.updatetraitement),
    path("delete/<int:id>/", views.delete),
# Constructeurs
    path("addc/", Constructeurs_views.add),
    path("traitementc/", Constructeurs_views.traitement),
    path("indexc", Constructeurs_views.index),
    path("affichec/<int:id>/", Constructeurs_views.affiche),
    path("updatec/<int:id>/", Constructeurs_views.update),
    path("updatetraitementc/<int:id>", Constructeurs_views.updatetraitement),
    path("deletec/<int:id>/", Constructeurs_views.delete),
]
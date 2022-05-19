from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LocomotiveForm(ModelForm):
    class Meta:
        model = models.Locomotive
        fields = ('nom', 'type', 'date_creation', 'pays_origine','description', 'Constructeur')
        labels = {
            'nom' : _('Nom'),
            'type' : _('Type de Motorisation') ,
            'date_creation' : _('Date de Création'),
            'pays_origine' : _('Pays d\'origine'),
            'description' : _('Description'),
            'Constructeur' : _('Constructeur')
        }

class ConstructeurForm(ModelForm):
    class Meta:
        model = models.Constructeur
        fields = ('nom', 'siege_social', 'date_creation', 'pays_origine','description')
        labels = {
            'nom' : _('Nom'),
            'siege_social' : _('Emplacement du Siège Social') ,
            'date_creation' : _('Date de Création'),
            'pays_origine' : _('Pays d\'origine'),
            'description' : _('Description')
        }
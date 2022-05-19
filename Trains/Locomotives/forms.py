from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LocomotiveForm(ModelForm):
    class Meta:
        model = models.Locomotive
        fields = ('nom', 'type', 'date_creation', 'pays_origine','description')
        labels = {
            'nom' : _('Nom'),
            'type' : _('Type de Motorisation') ,
            'date_creation' : _('Date de Création'),
            'pays_origine' : _('Pays d\'origine'),
            'description' : _('Description')
        }
from django.forms import ModelForm
from .models import Factory
# If we segrate management of workstations and tasks from factory we will need to import that model here.

class FactoryForm(ModelForm):
    class Meta:
        model = Factory
        fields = "__all__"
    pass
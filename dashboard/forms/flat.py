from django.forms import ModelForm
from dashboard.models import Flat

class FlatForm(ModelForm):
    class Meta:
        model = Flat
        fields = '__all__'
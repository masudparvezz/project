from django.forms import ModelForm
from dashboard.models import Shop
class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
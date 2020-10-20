from django.forms import ModelForm
from .models import Data

class UpdateForm(ModelForm):
    class Meta:
        model = Data
        fields = [
            'Latitude',
            'Longitude', 
            'Unique_Squirrel_ID',
            'Shift',
            'Date',
            'Age',
        ]

class CreateForm(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'


from django import forms
from stores.models import Store

    
class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 5:
            self.add_error('value', 'Valor minimo do item deve ser 5,00 $')
        return value
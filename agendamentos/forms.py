from django import forms

class AgendamentoForm(forms.Form):
    data = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))
    # Outros campos necessários, como nome, telefone, etc.
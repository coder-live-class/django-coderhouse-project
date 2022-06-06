from django import forms


class HomeworkForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre de la Entrega')
    due_date = forms.DateField(
        label='Fecha de Entrega',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    is_delivered = forms.BooleanField(label='Entregado', required=False)

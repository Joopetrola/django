from django import forms 


class pedidoForms(forms.Form):

    quantidade_forms=forms.CharField(
        label='Quantidade:', 
        required=True, 
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Quantidade',
                'type': 'number'
                }
            )
        )

    nome_login=forms.CharField(
    label='Nome de Login', 
    required=True, 
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: João',
            }
        )
    )


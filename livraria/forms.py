from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(
        attrs={
            'class':'form-control','placeholder':'E-mail'
        }
    ))
    first_name=forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control','placeholder':'First Name'
        }

    ))

    last_name=forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control','placeholder':'Last Name'
        }

    ))

    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email','password1', 'password2')

    def __init__ (self, *args,**kwargs): # Método de contrução, atributos dos itens do formulário
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text='''
            <span class="form-text text-muted">
                <small> Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas </small>
            </span>
'''
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text='''
            <ul class="form-text text-muted small">
                <li>Senha deve ser única. </li>
                <li>Senha deve ser conter pelo menos 8 caracteres. </li>
                <li>Senha não deve ser totalmente numérica. </li>
            </ul>
'''
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text=''' 
   
<span class="form-text text-muted">
                <small> Digite a mesma senha digitada no campo anterior </small>
            </span>
'''
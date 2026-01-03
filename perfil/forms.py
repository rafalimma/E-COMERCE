from django import forms
from django.contrib.auth.models import User
from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario', )

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha',
    )
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação da Senha'
    )
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password',
                  'password2', 'email')

    def clean(self, *args, **kwargs): 
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        usuario_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')
        

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()
        
        error_usuario_existe = 'Usuário ja existe'
        error_email_existe = 'email ja existe'
        error_senha_confere = 'As duas senhas não conferem'
        error_senha_pequena = 'A senha deve conter pelo menos 6 caracteres'
        error_msg_required_field = 'Campo obrigatório!'

        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db.username:
                    validation_error_msgs['username'] = error_usuario_existe
            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_email_existe

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_senha_confere
                    validation_error_msgs['password2'] = error_senha_confere
                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_senha_pequena
                    
        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))
        else:

            if usuario_db:
                validation_error_msgs['username'] = error_usuario_existe

            if email_db:
                validation_error_msgs['email'] = error_email_existe

            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field
            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field

            if password_data != password2_data:
                validation_error_msgs['password'] = error_senha_confere
                validation_error_msgs['password2'] = error_senha_confere
            if len(password_data) < 6:
                validation_error_msgs['password'] = error_senha_pequena


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from AuthReg.models import User
from WebDes.models import zayavka, main_tovar
from django import forms


class UserLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Пароль'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Имя'}))

    class Meta:
        model = User
        fields = ('email', 'password', 'username')
class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'User'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Фамилия'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Почта'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder':'Телефон'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Пароль еще раз'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2', 'phone')
class  User_ProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'phone')
class forma_otpr(forms.ModelForm):
    CHOICES= [
        ('Строительство', 'Строительство' ),
        ('Ремонт', 'Ремонт'),
        ('Дизайн', 'Дизайн'),
    ]
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4'}))
    ur_lico = forms.BooleanField()
    work_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = zayavka
        fields = ('first_name', 'last_name', 'email', 'phone', 'ur_lico', 'work_type')
class Add_Tovar(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    ploshad = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    cost = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    image = forms.ImageField()
    class Meta:
        model=main_tovar
        fields = ('name', 'ploshad', 'cost', 'image')

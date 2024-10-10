from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect ('/Gracias/')
        else:
            form = NameForm
class RegistroVehiculosForm(UserCreationForm):
    marca = forms.CharField(required=True)

    class Meta:
        Model = User
        fields = ('modelo', 'serial carrocería', 'serial motor', 'categoría', 'precio')

        def save(self, commit=True):
            user = super(RegistroVehiculosForm, self).save(commit=False)
            if commit:
                user.save()
            return user
            
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
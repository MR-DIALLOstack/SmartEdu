from django import forms
from .models import User, Etablissement

class AdminSignupForm(forms.ModelForm):
    etablissement_nom = forms.CharField(max_length=100)
    etablissement_adresse = forms.CharField(widget=forms.Textarea)
    etablissement_telephone = forms.CharField(max_length=15)
    etablissement_email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'telephone', 'password']
        widgets = {'password': forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'admin'
        user.is_admin = True
        user.is_staff = True
        if commit:
            user.save()
            Etablissement.objects.create(
                nom=self.cleaned_data['etablissement_nom'],
                adresse=self.cleaned_data['etablissement_adresse'],
                telephone=self.cleaned_data['etablissement_telephone'],
                email=self.cleaned_data['etablissement_email'],
                directeur=user
            )
        return user

class EleveSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'date_naissance', 'adresse', 'telephone', 'password']
        widgets = {'password': forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'eleve'
        if commit:
            user.save()
        return user

class EnseignantSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'adresse', 'telephone', 'password']
        widgets = {'password': forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'enseignant'
        if commit:
            user.save()
        return user

class ParentSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'adresse', 'telephone', 'password']
        widgets = {'password': forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'parent'
        if commit:
            user.save()
        return user

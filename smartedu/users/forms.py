from django import forms
from .models import User, Etablissement

class AdminSignupForm(forms.ModelForm):
    etablissement_nom = forms.CharField(max_length=100)
    etablissement_adresse = forms.CharField(widget=forms.Textarea)
    etablissement_email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'telephone', 'password']
        widgets = {'password': forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
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

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Votre email"})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Votre mot de passe"})
    )

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
        fields = ['nom', 'prenom', 'email', 'adresse', 'password']
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
        fields = ['nom', 'prenom', 'email', 'adresse', 'password']
        widgets = {'password': forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'parent'
        if commit:
            user.save()
        return user

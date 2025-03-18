from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, Etablissement
from .forms import AdminSignupForm, EnseignantSignupForm, EleveSignupForm, ParentSignupForm, LoginForm


# Vue d'inscription de l'administrateur
def register_admin(request):
    if request.method == "POST":
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.role = "admin"
            admin.is_staff = True
            admin.save()
            

            # Création de l'établissement lié à cet administrateur

            Etablissement.objects.create(
                nom = form.cleaned_data["etablissement_nom"],
                adresse = form.cleaned_data["etablissement_adresse"],
                email = form.cleaned_data["email"],
                directeur = admin
            )
            messages.success(request, "Compte administrateur et établisssement créés avec succès")
            return redirect("login")
    else:
        form = AdminSignupForm()
    return render(request, "users/register_admin.html", {"form": form})

# Vue de connexion
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Connexion réussie.")
                return redirect("dashboard")
            else:
                messages.error(request, "Identifiants invalides.")

    else:
        form = LoginForm()
    return render(request, "users/login.html")

# Vue pour ajouter un enseignant
@login_required
def add_enseignant(request):
    if request.user.role != "admin":
        messages.error(request, "Seul un administrateur peut ajouter des enseignants")
        return redirect("dashboard")
    if request.methode == "POST":
        form = EnseignantSignupForm(request.POST)
        if form.is_valid():
            enseignant = form.save(commit=False)
            enseignant.role = "enseignant"
            enseignant.save()
            messages.success(request, "Enseignant ajouté avec succès.")
            return redirect("list_enseignant")
        
        else:
            form = EleveSignupForm()
        return render(request, "users/add_enseignant.html", {"form": form})

# Vue pour ajouter un élève
@login_required
def add_eleve(request):
    if request.user.role != "admin":
        messages.error(request, "Seul un administrateur peut ajouter un élève.")
        return redirect("dashboard")
    if request.method == "POST":
        form = EleveSignupForm(request.POST)
        if form.is_valid():
            eleve = form.save(commit=False)
            eleve.role ="eleve"
            eleve.save()
            messages.success(request, "Elève ajouté avec succès.")
            return redirect("list_eleves")
        else:
            form = EleveSignupForm()

        return render(request, "users/add_eleve.html", {"form": form})
    
# Vue pour ajouter un parent
@login_required
def add_parent(request):
    if request.user.role != "admin":
        messages.error(request, "Seul un administrateur peut ajouter des parents.")
        return redirect("dashboard")
    
    if request.method == "POST":
        form = ParentSignupForm(request.POST)
        if form.is_valid():
            parent = form.save(commit=False)
            parent.role = "parent"
            parent.save()
            messages.success(request, "Parent ajouté avec succès.")
            return redirect("list_parents")
        else:
            form = ParentSignupForm()
        return render(request, "users/add_parent.html", {"form": form})

# Liste des utilisateurs
@login_required
def list_eleves(request):
    if request.user.role != "admin":
        messages.error(request, "Accès non autorisé.")
        return redirect("dashboard")
    eleves = User.objects.filter(role="eleve")
    return render(request, "users/list_eleves.html", {"eleves": eleves})

@login_required
def list_enseignants(request):
    if request.user.role != "admin":
        messages.error(request, "Accès non autorisé.")
        return redirect("dashboard")
    parents = User.objects.filter(role="enseignant")
    return render(request, "users/list_enseignants.html", {"enseignants": parents})

@login_required
def list_parents(request):
    if request.user.role != "admin":
        messages.error(request, "Accès non autorisé.")
        return redirect("dashboard")

    parents = User.objects.filter(role="parent")
    return render(request, "users/list_parents.html", {"parents": parents})

# Vue du profil utilisateur
@login_required
def profile(request, user_id):
    utilisateur = get_object_or_404(User, id=user_id)
    return render(request, "users/profile.html", {"utilisateur": utilisateur})

# Vue du dashboard
@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")

# Vue pour la déconnexion
def user_logout(request):
    logout(request)
    return redirect("login")

# Vue de la page d'accueil
def home(request):
    return render(request, "users/home.html")

# Vue pour la liste des enseignants
def list_enseignants(request):
    return render(request, 'users/list_enseignants.html')

# Vue pour la liste des eleves
def list_eleves(request):
    return render(request, 'users/list_eleves.html')

# Vue pour la liste des parents
def list_parents(request):
    return render(request, 'users/list_parents.html')

# Vue pour la liste des enseignants
def liste_enseignants(request):
    return render(request, "users/list_enseignants.html")
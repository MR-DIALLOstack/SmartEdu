from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Créer un utilisateur normal"""
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Créer un administrateur avec tous les privilèges"""
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('enseignant', 'Enseignant'),
        ('eleve', 'Élève'),
        ('parent', 'Parent'),
    ]

    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    date_naissance = models.DateField(null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)

    
    # Champs spécifiques à l'administration Django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Utilisation de l'email comme identifiant principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'role']

    objects = UserManager()

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.role})"

class Etablissement(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField(unique=True)
    directeur = models.OneToOneField(User, on_delete=models.CASCADE, related_name="etablissement")

    def __str__(self):
        return self.nom

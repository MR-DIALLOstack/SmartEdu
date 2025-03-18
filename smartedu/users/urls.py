from django.urls import path
from .views import login_view, register_admin, dashboard, profile, user_logout, list_enseignants, list_eleves, list_parents

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_admin, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
    path("logout/", user_logout, name="logout"),
    path('enseignants/', list_enseignants, name='list_enseignants'),
    path('eleves/', list_eleves, name="list_eleves"),
    path('parents/', list_parents, name="list_parents"),
]

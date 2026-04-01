from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("add/", views.add_application, name="add_application"),
 # ✅ ADD THIS
    path("login/", auth_views.LoginView.as_view(template_name="tracker/login.html"), name="login"),
]



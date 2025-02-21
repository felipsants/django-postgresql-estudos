from django.contrib import admin
from django.urls import include, path
from .views import homepage  # Importa a view da homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("home", homepage, name="homepage"),  # Agora "/" acessa a homepage
]
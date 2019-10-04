from django.urls import path,include
from .views import basic_seeder

urlpatterns = [
    path('basicfake/', basic_seeder),
]

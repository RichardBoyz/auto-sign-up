from django.urls import path
from signin.views import sign_in
urlpatterns = [
    path('',sign_in)
]

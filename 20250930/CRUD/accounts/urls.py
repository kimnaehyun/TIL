from django.urls import path
from . import views

# url naming pattern
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login')
]

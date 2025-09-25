from django.urls import path
from . import views

# url_naming pattern
app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # variable routing
    # pk의 변수에 할당된 값은 views.py의 detail함수의 pk 매개변수로
    path('<int:pk>/', views.detail, name='detail'),
]
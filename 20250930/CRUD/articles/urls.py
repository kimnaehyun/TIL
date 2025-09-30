from django.urls import path

from . import views

# url naming pattern
app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index'),
    # variable routing
    # pk의 변수에 할당된 값은 views.py의 detail함수의 pk 매개변수로
    path('<int:pk>/', views.detail, name = 'detail'),
    # 클라이언트에서 입력한 데이터를 DB에 저장
    path('create/', views.create, name = 'create'),
    # 단일 게시글 조회 후 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),

    path('<int:pk>/update/', views.update, name = "update"),
]
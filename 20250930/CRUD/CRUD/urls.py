from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # url 매핑
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls'))
]

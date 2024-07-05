from django.contrib import admin
from django.urls import path, include
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
    path('', admin.site.urls, name='home'),
]

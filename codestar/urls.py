from django.contrib import admin
from django.urls import path, include          # ← add include
from blog import views as index_views          # ← import the views with an alias

urlpatterns = [
    path('', index_views.index, name='index'), # ← add this line (root URL)
    path('admin/', admin.site.urls),
]
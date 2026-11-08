
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

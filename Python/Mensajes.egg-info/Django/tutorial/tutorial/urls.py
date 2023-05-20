from django.contrib import admin
from django.urls import path
from blog.views import home, post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('blog/<id>', post, name="post")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

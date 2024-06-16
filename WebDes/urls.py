from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from WebDes import views
urlpatterns = [
        path('', views.index, name="index"),
    path('sad@123/', include('AuthReg.urls', namespace='AuthReg')),
    path('catalogue', views.katalog, name="katalog")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
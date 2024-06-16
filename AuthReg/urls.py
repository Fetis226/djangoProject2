from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from AuthReg.views import login
app_name = "AuthReg"

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', views.registration, name="registration"),
    path('check/', views.auth_check, name='auth_check'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_profile/forma_otpravki/', views.Zayavka, name='zayavka'),
    path('BabyBuild/admin_panel/', views.admins_panel, name='ADMIN_panel'),
    path('deleteTovar/<int:id>', views.deleteTovar, name='deleteTovar'),
    path('Admin_Panel/Add_tovar', views.Add_Tovars, name='add_tovars'),
    path('deleteZayvka/<int:id>', views.deleteZayavka, name='deleteZayavka'),
    path('AcceptZayvka/<int:id>', views.AcceptZayavka, name='AcceptZayavka')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
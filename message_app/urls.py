from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Main
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    # path('<str:string>/', views.redirect_page, name='redirect_page'),
    # Login / Register
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page,  name='register'),
    # Contents
    path('chats/', views.chats_page, name='chats'),
    path('chats/<int:id>', views.chats_convo_page, name='convo'),
    path('groups/', views.groups_page, name='groups'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('notifications/', views.notifications_page,  name='notifications'),
    path('settings/', views.settings_page,  name='settings'),
    # Profile
    path('profile/', views.profile_page,  name='profile'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/change_profile', views.change_profile, name='change profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

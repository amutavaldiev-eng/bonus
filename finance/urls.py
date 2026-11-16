from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('add_wallet/', add_wallet, name='add_wallet'),
    path('read_wallet/', read_wallet, name='read_wallet'),
    path('update_wallet/<int:id>/', update_wallet, name='update_wallet'),
    path('delete_wallet/<int:id>/', delete_wallet, name='delete_wallet'),
    path('deposit/', deposit, name='deposit'),
    path('withdraw/', withdraw, name='withdraw'),
    path('add_history/', add_history, name='add_history'),
    path('read_history/', read_history, name='read_history'),
    path('update_history/<int:id>/', update_history, name='update_history'),
    path('delete_history/<int:id>/', delete_history, name='delete_history'),
    path('add_category/', add_category, name='add_category'),
    path('see_category/', see_category, name='see_category'),
    path('update_category/<int:id>/', update_category, name='update_category'),
    path('delete_category/<int:id>/', delete_category, name='delete_category'),
]
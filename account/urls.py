from django.conf.urls import url
from .views import nav_login, registration, nav_profile, logout

urlpatterns = [
    url(r'login/', nav_login, name='login'),
    url(r'registration/', registration, name='registration'),
    url(r'profile/', nav_profile, name='profile'),
    url(r'logout/', logout, name='logout'),

]

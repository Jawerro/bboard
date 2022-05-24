from email.errors import NoBoundaryInMultipartDefect
from django.urls import path
from .views import BBLogoutView, BbLoginView, index, other_page, profile
from .views import ChangeUserInfoView, BBPaswordChangeView, RegisterUserView, RegisterDoneViews
app_name = 'main'
urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/login/', BbLoginView.as_view(), name='login'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password_change/', BBPaswordChangeView.as_view(), name='password_change'),
    path('accounts/register/done/', RegisterDoneViews.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
]
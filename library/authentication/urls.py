from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account/', views.account, name='account'),
    path('edit/<int:pk>', views.edit_user, name='edit_user'),
]
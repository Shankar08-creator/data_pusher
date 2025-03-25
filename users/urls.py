from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # ✅ Only POST
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', UserListView.as_view(), name='user-list'),  # ✅ List all users at /api/users/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

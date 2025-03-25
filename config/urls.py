from django.contrib import admin  # ✅ Import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountViewSet
from destinations.views import DestinationViewSet
from users.views import RegisterView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse

# Router for API endpoints
router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)

# Homepage view (redirect `/` to `/api/`)
def homepage(request):
    return HttpResponse("<h1>Welcome to the API</h1><p>Go to <a href='/api/'>/api/</a> for the API.</p>")

urlpatterns = [
    # path('admin/', admin.site.urls),  

    path('', homepage, name='homepage'),  
    path('api/', include(router.urls)),  

    # Authentication Endpoints
    path('api/users/register/', RegisterView.as_view(), name='register'),
    path('api/users/login/', LoginView.as_view(), name='login'),
    path('api/users/logout/', LogoutView.as_view(), name='logout'),

    # JWT Token Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# from django.urls import path, include
# from django.contrib import admin

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # ✅ Users endpoints
    path('api/destinations/', include('destinations.urls')),  # ✅ Add this line
]


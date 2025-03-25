from django.urls import path
from .views import DestinationListView  # ✅ Import your view

urlpatterns = [
    path('', DestinationListView.as_view(), name='destination-list'),  # ✅ Ensure this line is present
]

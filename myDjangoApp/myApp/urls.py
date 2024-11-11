# Import the views you want to use and then create URL patterns for each view. 

from django.urls import path
from . import views  # Import your views

# define URL patterns using the urlpatterns list.

urlpatterns = [
    path('user-data/', views.user_data_view, name='user-data'),
    path('app-usage-data/', views.app_usage_data_view, name='app-usage-data'),
    path('transaction-data/', views.transaction_data_view, name='transaction-data'),
    path('api/authenticate/', UserAuthenticationView.as_view(), name='user-authenticate'), 
    # change user-authentication if needed
]

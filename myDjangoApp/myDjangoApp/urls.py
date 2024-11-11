# urls.py file in a Django app is used to define URL patterns that map to views.
# It specifies how URLs are routed to view functions within the app.

"""
URL configuration for myDjangoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# configure your Django project's URLs to map to the view (given below code )so that you can access it via a web browser.

from django.contrib import admin
from django.urls import path, include

# Replace 'your-app/' with the URL prefix you want to use for your app's views.
# This URL prefix will be added to the URLs you defined in your app's urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    # path() function is used to define URL patterns in Django. 
    # include() function is used to include URLs defined in app-specific urls.py files into the project's URL configuration.
    path('myApp/', include('myApp.urls')),  # Include your app's URLs here

]

# his configuration will make your app's views accessible under URLs like http://your-domain/myDjangoApp/user-data/, 
# http://your-domain/myDjangoApp/app-usage-data/, and http://your-domain/myDjangoApp/transaction-data/.

# Once you've configured your URLs as described above, you can access your views in 
# a web browser by visiting URLs like http://your-domain/user-data/, 
# http://your-domain/app-usage-data/, and http://your-domain/transaction-data/

from django.contrib import admin
from django.urls import path, include

from accounts.urls import *


urlpatterns = [
    path('account/', include('accounts.urls')),

    path('admin/', admin.site.urls),
]

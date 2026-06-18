
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('gs/', admin.site.urls),
    path('', include('blog.urls'))
]

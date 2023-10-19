
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('watch/',include('watchlist_app.api.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('user_app.api.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# append the static path 

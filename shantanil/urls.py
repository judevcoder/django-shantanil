from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('dashboard.urls'), name='dashboard')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

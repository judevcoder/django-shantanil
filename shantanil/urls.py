from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from dashboard import views as dash_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dash_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', dash_views.signup, name='signup'),
    path('login/', dash_views.login_user, name='login'),
    path('dashboard/', dash_views.dashboard, name='dashboard'),
    path('', include('dashboard.urls'), name='dashboardpage')
    # path('', include('dashboard.urls'), name='dashboard')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

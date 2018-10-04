from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('connection/', views.connection, name='connection'),
    path('connection/adapter/', views.connection_adapter, name='adapter'),
    # path('', login_required(views.DashboardView.as_view()), name='dashboard_page')
]
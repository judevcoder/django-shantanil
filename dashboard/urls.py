from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='dashboard_page'),
    path('', RedirectView.as_view(url='login', permanent=False), name='index'),

    path('login/', views.LoginView.as_view(),name='login'),
    # url(r'^logout/', views.logout, name='logout'),
]
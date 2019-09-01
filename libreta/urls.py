from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('main/', views.MainView.as_view(), name='main'),
	path('', views.LibretaView.as_view(), name='list_libreta_familia'),
	path('create/', views.LibretaCreateView.as_view(), name='create_libreta_familia'),
    path('edit/<int:pk>', views.LibretaUpdateView.as_view(), name='edit_libreta_familia'),
    path('delete/<int:pk>', views.LibretaDeleteView.as_view(), name='delete_libreta_familia'),
    path('trabajo/', views.TrabajoView.as_view(), name='list_libreta_trabajo'),
	path('create-trabajo/', views.TrabajoCreateView.as_view(), name='create_libreta_trabajo'),
    path('edit-trabajo/<int:pk>', views.TrabajoUpdateView.as_view(), name='edit_libreta_trabajo'),
    path('delete-trabajo/<int:pk>', views.TrabajoDeleteView.as_view(), name='delete_libreta_trabajo'),]
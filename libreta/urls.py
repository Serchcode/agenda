from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.Libreta.as_view(), name='list_libreta_familia'),
	path('create/', views.LibretaCreateView.as_view(), name='create_libreta_familia'),
    path('edit/<int:pk>', views.LibretaUpdateView.as_view(), name='edit_libreta_familia'),
    path('delete/<int:pk>', views.LibretaDeleteView.as_view(), name='delete_libreta_familia'),]
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
	path('cars/', views.CarList.as_view(), name='car-list'),
	path('cars/<int:pk>', views.CarDetail.as_view(), name='car-detail'),
	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetailt.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
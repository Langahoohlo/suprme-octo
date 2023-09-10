from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboardv2/', views.dashboardv2, name='dashboardv2'),
    path('myprofile/', views.media, name='myprofile'),
    path('myprofile/<int:created_by_id>/', views.myprofile_view, name='myprofile'),
    path('delete_media/<int:media_item_id>/', views.delete_media, name='delete_media'),

]

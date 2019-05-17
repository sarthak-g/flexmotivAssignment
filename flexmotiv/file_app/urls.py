from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('create/',views.FileCreateView.as_view(),name='file_create'),
    path('view/',views.FileListView.as_view(),name='file_view'),
    # path('view/',FileCreateView.as_view(),name='file_create'),

]

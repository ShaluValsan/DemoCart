from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cvbhome/',views.Tasklistview.as_view(),name='cvbhome'),
    path('cvbdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cvbdetail'),
    path('cvbupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cvbupdate'),
    path('cvbdelete/<int:pk>/', views.Deleteview.as_view(), name='cvbdelete')
    #path('details',views.details,name='details')

]
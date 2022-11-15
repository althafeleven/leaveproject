from django.urls import path
from django.conf import urls
from. import views


urlpatterns = [
    path('',views.home, name='aelog.html'),
    path('emp',views.emp,name='aelog.html'),
    path('along',views.ad,name='aelog.html'),
    path('employee',views.employee,name='aelog.html'),
    
   
    path('empleave',views.empleave,name='leaveapply.html'),
    path('leavedetails',views.leavedetails,name='leavedetails'),
    path('leaveedit/<int:i>/',views.leaveedit,name='leaveedit'),
    path('leaveedit1/<int:i>/',views.leaveedit1,name='leaveedit1'),
    path('leaveapprove/<int:i>/',views.leaveapprove,name='leaveapprove'),
    path('leavereject/<int:i>/',views.leavereject,name='leavereject'),
    path('leavestatus',views.leavestatus,name='leavestatus'),
]
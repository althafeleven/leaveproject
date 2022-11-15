from django.contrib import admin
from. models import Login,Register,Leaveapply,Leaveapprove,Leavereject,Leavedetails
# Register your models here.
admin.site.register(Login)
admin.site.register(Register)
admin.site.register(Leaveapply)
admin.site.register(Leaveapprove)
admin.site.register(Leavereject)
admin.site.register(Leavedetails)
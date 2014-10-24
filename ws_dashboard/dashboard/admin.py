from django.contrib import admin

from dashboard.models import *

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Call)
admin.site.register(Message)
admin.site.register(Data)


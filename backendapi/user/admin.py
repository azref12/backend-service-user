from django.contrib import admin
from account.models import user_detail
from django.contrib.auth.models import User

admin.site.register(User)
admin.site.register(user_detail)

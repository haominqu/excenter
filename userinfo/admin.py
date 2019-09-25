# django
from django.contrib import admin
from django.contrib.auth.hashers import make_password

# selfproject
from .models import UserInfo, Guest, UserDetail
from userinfo.fourrandom import generate_code

# base
import time

# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # obj.uu_id = str(int(round(time.time() * 1000))) + generate_code()

        obj.password = make_password(obj.password, None, 'pbkdf2_sha256')
        obj.save()


class GuestAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.user.uu_id = str(int(round(time.time() * 1000))) + generate_code()
        obj.save()
        obj.user.save()


class UserDetailAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.user.uu_id = str(int(round(time.time() * 1000))) + generate_code()
        obj.save()
        obj.user.save()


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(UserDetail, UserDetailAdmin)
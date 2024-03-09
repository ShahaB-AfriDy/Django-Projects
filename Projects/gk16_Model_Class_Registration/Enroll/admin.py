from django.contrib import admin
from Enroll.models import Student
# Register your models here.


# class Student_Admin(admin.ModelAdmin):
#     list_display = ('id','Name','Reg_No',"Email")

# admin.site.register(Student,Student_Admin)

admin.site.register(Student)


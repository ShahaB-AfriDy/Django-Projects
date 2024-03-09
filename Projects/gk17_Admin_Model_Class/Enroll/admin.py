from django.contrib import admin
from Enroll.models import Student
# Register your models here.



@admin.register(Student)

class Student_Admin(admin.ModelAdmin):
    list_display = ('id','Name',"Reg_No","Email","Date","Description")
    # list_display is variable write as it's
    # django write as it's that's why




#-----------------------same the above just used decorator
# class Student_Admin(admin.ModelAdmin):
#     list_display = ('id','Name',"Reg_No","Email","Description")


# admin.site.register(Student,Student_Admin)    
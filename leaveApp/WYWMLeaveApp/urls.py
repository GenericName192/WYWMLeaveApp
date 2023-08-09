from django.contrib import admin
from django.urls import path
from views import dashBoard, companyHolidays, leaveApproval, leaveBalance, leaveRequest, profileSettings, loginUser

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashBoard, name="dashBoard"),
    path("companyHolidays", companyHolidays, name="companyHolidays"),
    path("leave/approval", leaveApproval, name="leaveApproval"),
    path("leave/balance", leaveBalance, name="leaveBalance"),
    path("leave/request", leaveRequest, name="leaveRequest"),
    path("profileSettings", profileSettings, name="profileSettings"),
    path("login", loginUser, name="loginUser"),
]
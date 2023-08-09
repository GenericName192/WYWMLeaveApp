from django.shortcuts import render

# Create your views here.
def dashBoard(request):
    return render(request, "WYWMLeaveApp/dashboard.html")

def companyHolidays(request):
    return render(request, "WYWMLeaveApp/company_holidays.html")

def leaveApproval(request):
    return render(request, "WYWMLeaveApp/leave_approval.html")

def leaveBalance(request):
    return render(request, "WYWMLeaveApp/leave_balance.html")

def leaveRequest(request):
    return render(request, "WYWMLeaveApp/leave_request.html")

def profileSettings(request):
    return render(request, "WYWMLeaveApp/profile_settings.html")

def loginUser(request):
    return render(request, "WYWMLeaveApp/login.html")
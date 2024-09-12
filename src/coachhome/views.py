from django.shortcuts import render

# Create your views here.
#from dashboard.views import dashboard_view

def coach_home_page(request):

    return render(request, "coach/home.html")

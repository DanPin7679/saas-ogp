from django.shortcuts import render

# Create your views here.
#from dashboard.views import dashboard_view

def player_home_page(request):
    # if request.user.is_authenticated:
    #     return dashboard_view(request)
    return render(request, "player/home.html")

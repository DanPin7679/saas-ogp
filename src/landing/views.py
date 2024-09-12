from django.shortcuts import render

# Create your views here.
from playerhome.views import player_home_page
from coachhome.views import coach_home_page

def landing_page(request):
    user = request.user
    if user.is_authenticated:
        print(
            "users perm", 
            user.has_perm("subscriptions.free"),
            user.has_perm("subscriptions.basic"),
            user.has_perm("subscriptions.premium"),
            user.has_perm("subscriptions.coach"))
        if user.has_perm("subscriptions.coach"):
            return coach_home_page(request)
        else:
            return player_home_page(request)
    return render(request, "landing/main.html")

from django.shortcuts import render
from .models import Meeting

# Create your views here.
def meetings_page(request):
    
    return render(request, 'meetings/main.html')

def meetings_list(request):
    meetings=Meeting.objects.all()
    context = {'meetings': meetings}

    if request.htmx:
        return render(request, 'meetings/partials/meetings-container.html', context)

    return render(request, 'meetings/meetings-list.html', context)

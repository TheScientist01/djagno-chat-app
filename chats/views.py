from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

# Create your views here.

def index(request):
    return render(request, 'chats/index.html')

@login_required
def room(request, room_name):
    return render(request, 'chats/room.html', {
        'room_name': room_name,
        'username': mark_safe(json.dumps(request.user.username)),
    })




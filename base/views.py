# from multiprocessing import context
# import re
from django.shortcuts import render, redirect
# from django.http import HttpResponse
# Create your views here.
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name': 'Lets learn python'},
#     {'id':2, 'name': 'Design with me'},
#     {'id':3, 'name': 'Frontend developer'},
# ]
rooms = Room.objects.all()


# def room(request):
#     return HttpResponse("Room page")

def home(request):  
    rooms = Room.objects.all()
    context = {'roo' : rooms}
    return render(request, 'home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'roo': room}
    return render(request, 'room.html',context)

# def room(request,pk):
#     room = None
#     for i in rooms:
#         if i['id'] == int(pk):
#             room = i
#         else:
#             context= {'roo':None}
#         context = {'roo' : room}
#     return render(request, 'room.html',context)

# def createroom(request):
    
#     form = RoomForm()
    
#     if request.method == 'POST':
#         # print(request.POST.get('name'))
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')


#     context = {'form': form}

#     return render(request, 'room_form.html',context)
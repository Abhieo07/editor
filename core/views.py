from django.shortcuts import render
from .models import Core
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        text = request.POST['text']
        video = request.FILES.get('video')
        #time = datetime.now
        if video and text:
            core = Core.objects.create(text=text,video=video)
            core.save()
            messages.success(request,"Upload Successfull")
        else:
            messages.error(request,"Upload again")

    return render(request,'core/index.html',{
        'last':Core.objects.last()
    })
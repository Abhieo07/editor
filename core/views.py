from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from .models import Core
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = None
    if request.method == 'POST':
        text = request.POST['text']
        video = request.FILES.get('video')
        #time = datetime.now
        context = {'last':video}
        if video and text:
            core = Core.objects.create(text=text,video=video)
            core.save()
            messages.success(request,"Upload Successfull")
            return HttpResponseRedirect('success')
        else:
            messages.error(request,"Upload again")
            raise Http404(request)

    return render(request,'core/index.html',context)

def success(request):
    #lastfile = get_object_or_404(Core,text=str)
    #print(lastfile)
    return render(request,'core/success.html',{
        'last': Core.objects.last()
    })
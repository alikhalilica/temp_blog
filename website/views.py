from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactTicketsForm
# root page
def index(request):
    return render(request,"website/index.html")
def about(request):
    return render(request,"website/about.html") 
def contact(request):
    if (request.method == 'POST'):
        form = ContactTicketsForm(data=request.POST) #**kwarg *arg
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            #return HttpResponse("contact saved")
            messages.success(request,'your ticket have been recieved')
            return HttpResponseRedirect(request.path_info) #path_info == url client 
    else:
        form = ContactTicketsForm()
        context = {'form':form}
        return render(request, "website/contact.html",context)

from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse
from django.urls import reverse
from first_app.forms import NewUser
# Create your views here.
def index(request):
    mydict={"name":"Zeeshan"}
    return render(request,'first_app/index.html',mydict)

def users(request):
    form = NewUser()

    if request.method=="POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Error')

    return render(request,'first_app/users.html',{'form':form})

def thankyou(request):
    mydict=request.session.get('s')
    # del mydict['csrfmiddlewaretoken']
    return render(request,'first_app/thankyou.html',mydict)

def form_name_view(request):

    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("validation succcess")
            ctxt={'name':form.cleaned_data['name'],
            'email':form.cleaned_data['email'],
            'text':form.cleaned_data['text']}
            request.session['s']=ctxt
            thankyou_url=reverse('thankyou')
            return redirect(thankyou_url)

        else:
            return render(request,'first_app/form_page.html',{'form':form})
    else:
        form=forms.FormName()
        return render(request,'first_app/form_page.html',{'form':form})

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration(request):

    if request.method == 'GET':
        form = RegistrationForm()

        return render(request, 'registration.html', {'form':form} )
    
    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ads')
        else:
            form = RegistrationForm()
            return render(request, 'registration.html', {'error':form.error_messages,'form':form})



def authorization(request):
    return render(request, 'authorization.html')
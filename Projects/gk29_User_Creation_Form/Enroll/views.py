from django.shortcuts import render
from Enroll.forms import User_From
from django.contrib import messages
# Create your views here.


def Home(request):
    if request.method == 'POST':
        form = User_From(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Saved: {username}")
    else:
        form = User_From()
    return render(request,template_name='Enroll/home.html',
                  context={"form":form})

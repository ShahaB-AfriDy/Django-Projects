# views.py
from django.shortcuts import render, redirect
from dropdownlist.form import MyForm  

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Do something with the form data, e.g., save to the database
            # You can access the selected option using form.cleaned_data['my_field']
            # For now, let's just print it
            print(form.cleaned_data['my_field'])
            # return redirect('success_page')  # Redirect to a success page
    else:
        form = MyForm()

    return render(request, 'index.html', {'form': form})

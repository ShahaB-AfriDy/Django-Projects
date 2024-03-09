from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.

def home(request):
    context  = {'home':'active'}
    return render(request,template_name="home.html",context=context)


from django.http import HttpResponse
from django.conf import settings
import os

def download_file(request):
    file_name = 'Shahab_Afridy_CV.pdf'
    file_path = os.path.join("E:\\Python in Sublime\\DJango Framework\\Resume\\Shahab_Afridy\\Main\\static\\img", file_name)  
    
    try:
        # Check if the file exists
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

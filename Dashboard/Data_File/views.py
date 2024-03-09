from django.shortcuts import render,redirect,HttpResponse
import pandas as pd

Columns = None
df = None

def Home(request):
    return render(request, template_name='home.html')

def Display_Summary(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            global Columns,df
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)
            Columns = df.select_dtypes(include=['number']).columns.tolist()
            return render(request,'display_csv.html', {'Columns': Columns})
        else:
            return redirect("/")
    

def Calculated(request,column):
    if request.method == "GET":
        statistics = {}
        column_data = df[column]
        statistics = {
            'sum': round(column_data.sum(),2),
            'min': round(column_data.min(),2),
            'max': round(column_data.max(),2),
            'range': round(column_data.max() - column_data.min(),2),
            'mean': round(column_data.mean(),2),
            'median': round(column_data.median(),2),
            'std': round(column_data.std(),2),
            'var': round(column_data.var(),2),
            'count': round(column_data.count(),2)
        }
    return render(request,'display_csv.html',{"Summary":statistics,'Columns': Columns,'feature':column})







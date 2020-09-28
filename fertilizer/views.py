from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from .models import FreResults



def findex(request):
    context={'name':'fertilizer'}
    return render(request,'fertilizer/index.html',context)


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Temperature= float(request.POST.get('Temperature'))
        Humidity = float(request.POST.get('Humidity'))

        Moisture = float(request.POST.get('Moisture'))

        Stype =float(request.POST.get('Stype'))
        Ctype = float(request.POST.get('Ctype'))
        Nitrogen = float(request.POST.get('Nitrogen'))
        Potassium = float(request.POST.get('Potassium'))
        Phosphorous = float(request.POST.get('Phosphorous'))

        # Unpickle model
        import pickle
        model = pd.read_pickle(r"C:\Users\dell\Desktop\new_model.pickle")


        # Make prediction
        result = model.predict([[Stype, Ctype, Temperature, Humidity, Moisture, Potassium, Phosphorous, Nitrogen]])

        classification = result[0]

        FreResults.objects.create(Stype=Stype, Ctype=Ctype,Temperature=Temperature,Humidity=Humidity,Moisture=Moisture,Potassium=Potassium,Phosphorous=Phosphorous,Nitrogen=Nitrogen,classification=classification)


        return JsonResponse({'result': classification,'Stype':Stype, 'Ctype':Ctype,'Temperature':Temperature,'Humidity':Humidity,'Moisture':Moisture,'Potassium':Potassium,'Phosphorous':Phosphorous,'Nitrogen':Nitrogen },
                            safe=False)

def view_results(request):
    data={"dataset": FreResults.objects.all()}
    return render(request,'fertilizer/result.html',data)

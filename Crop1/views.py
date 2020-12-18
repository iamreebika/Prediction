from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from django.urls import reverse
#from .models import CropResults


def index(request):
    context={'name':'Crop1'}
    # return HttpResponseRedirect(reverse("Crop1:submit_prediction"))
    context.update({'crop_url': reverse("Crop1:submit_prediction")})
    return render(request,'Crop1/index.html',context)



def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Temperature= float(request.POST.get('Temperature'))
        Humidity = float(request.POST.get('Humidity'))

        Moisture = float(request.POST.get('Moisture'))

        Stype =float(request.POST.get('Stype'))
        Ph = float(request.POST.get('Ph'))




        # Unpickle model
        import pickle
        model = pd.read_pickle(r"C:\Users\dell\Desktop\new_model1.pickle")


        # Make prediction
        result = model.predict([[Stype, Ph, Temperature, Humidity, Moisture]])

        classification = result[0]

        #FreResults.objects.create(Stype=Stype, Ctype=Ctype,Temperature=Temperature,Humidity=Humidity,Moisture=Moisture,Potassium=Potassium,Phosphorous=Phosphorous,Nitrogen=Nitrogen,classification=classification)


        return JsonResponse({'result': classification,'Stype':Stype, 'Ph':Ph,'Temperature':Temperature,'Humidity':Humidity,'Moisture':Moisture },
                            safe=False)


#def view_results(request):

       #data={"dataset": CropResults.objects.all()}
       #return render(request,'Crop1/result.html',data)





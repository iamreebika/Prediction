from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from .models import CropResults



def index(request):
    context={'name':'Crop'}
    # return HttpResponseRedirect(reverse("Crop1:submit_prediction"))
    context.update({'crop_url': reverse("Crop1:submit_prediction")})
    return render(request,'Crop1/index.html',context)


def predict_chances1(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Temperature= float(request.POST.get('Temperature'))
        Humidity = float(request.POST.get('Humidity'))

        Moisture = float(request.POST.get('Moisture'))

        Soiltype =float(request.POST.get('Soiltype'))
        pH = float(request.POST.get('pH'))


        # Unpickle model
        import pickle
        model = pd.read_pickle(r"C:\Users\dell\Desktop\new_model.pickle")


        # Make prediction
        result = model.predict([[Soiltype, pH, Temperature, Humidity, Moisture]])

        classification = result[0]

        CropResults.objects.create(Soiltype=Soiltype, pH=pH,Temperature=Temperature,Humidity=Humidity,Moisture=Moisture,classification=classification)


        return JsonResponse({'result': classification,'Soiltype':Soiltype, 'pH':pH,'Temperature':Temperature,'Humidity':Humidity,'Moisture':Moisture },
                            safe=False)

def view_results(request):
  data={"dataset": CropResults.objects.all()}

  return render(request,'Crop1/result.html',data)

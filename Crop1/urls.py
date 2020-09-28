from django.urls import path
from .views import index,predict_chances1,view_results

app_name='Crop1'





urlpatterns=[
    path('', index, name='Crop1'),
    path('crop/',predict_chances1,name='submit_prediction'),
    path('cresults/',view_results,name='cresults'),
]

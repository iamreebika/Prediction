from django.urls import path
from .views import findex,predict_chances,view_results

app_name = "fertilizer"



urlpatterns=[
    path('', findex, name='fertilizer'),
    path('fertilizer/',predict_chances,name='submit_prediction'),
    path('results/',view_results,name='results'),
]

from django.urls import path


from .views import index, predict_chances

app_name='Crop1'





urlpatterns=[
    path('', index, name='Crop1-name'),
    path('Crop1/',predict_chances,name='submit_prediction'),
    #path('Crop1/results/',view_results,name='cresults'),
]

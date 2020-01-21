from django.urls import path, include
from . import views 
from census.views import census_upload


urlpatterns = [
    path('', views.CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
    path('upload-csv/', census_upload, name="census_upload"),
]


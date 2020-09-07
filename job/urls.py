from django.urls import include, path

from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('fav/<str:slug>', views.post_fav, name='a'),
    path('favourite', views.post_favourite_list, name='post_favourite_list'),
    path('your/apply',views.Apply_view,name='Apply_view'),
    path('apply',views.Apply_view_2,name='Apply_view_2'),
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    path('delete/<str:slug>', views.delete_job, name='delete_job'),
    path('api/jobs', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),
    path('api/v2/jobs', api.JobListApi.as_view(), name='job_list_api'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='job_detail_api'),

]

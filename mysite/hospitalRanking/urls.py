from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'hospitalRanking'

urlpatterns = [
    # .com/hospitalRanking/
    url(r'^$', TemplateView.as_view(template_name='hospitalRanking/index.html'), name='index'),
    # .com/hospitalRanking/submitRankingForm
    url(r'^submitRankingForm', views.submit_ranking_form, name='submit_ranking_form'),
    # .com/hospitalRanking/results
    url(r'^results', TemplateView.as_view(template_name='hospitalRanking/results.html'), name='results'),
    # .com/hospitalRanking/hospital/
    url(r'^hospital/(?P<hospital_id>[\w+0-9+]+)/$', views.get_hospital, name='getHospital'),
]

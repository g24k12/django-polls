from django.urls import path

from . import views

app_name = 'polls'
urlpatterns=[
    path('', views.index, name="index"),

    #adding the polls path eg:/pools/2/
    path("<int:question_id>/",views.detail,name = 'detail'),

    #path for results/polls/2/results
    path("<int:question_id>/results/",views.results,name = 'results'),

    # path for results/polls/2/vote
    path("<int:question_id>/vote/",views.vote,name = 'vote')
]
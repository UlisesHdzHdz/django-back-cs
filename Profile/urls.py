from django.urls import path, include, re_path

from Profile.views import ProfileTable, ProfileTableDetail, UserProfile

urlpatterns = [
    re_path(r'^profile', ProfileTable.as_view()),
    re_path(r'^perfil/(?P<pk>\d+)/$', ProfileTableDetail.as_view()),
    re_path(r'^data/(?P<pk>\d+)/$', UserProfile.as_view()),

]

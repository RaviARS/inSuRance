from django.urls import path
from django.conf.urls import url
from .views import PolicyListView, PolicyDetailView
from .views import PolicyAdd, PolicySearchAPI, PolicyChartAPI
from .views import index, policy_details, policy_chart, policy_edit, policy_add


urlpatterns = [

    path('api/v1/policys/bulk_add/', PolicyAdd.as_view(), name='policy-bulkadd'),
    path('api/v1/policys/', PolicyListView.as_view(), name='policy-add'),
    path('api/v1/policys/<int:id>/', PolicyDetailView.as_view()),

    # url(r'api/v1/policy/pid/(?P<cid>[0-9A-Fa-f\-]+)/$', PolicyAPI.as_view()),
    url(r'api/v1/policy/search/', PolicySearchAPI.as_view()),
    url(r'api/v1/policy/chart/', PolicyChartAPI.as_view()),

    path('', index, name='index'),
    path('ui/policy-detail', policy_details, name='policy-details'),
    path('ui/policy-chart', policy_chart, name='policy-chart'),
    path('ui/policy-add', policy_add, name='policy-add'),
    path('ui/policy-edit', policy_edit, name='policy-edit'),


]

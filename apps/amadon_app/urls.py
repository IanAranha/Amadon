from django.conf.urls import url, include
from . import views


def test(request):
    print '#' * 50
    print 'App level good'
    print '@' * 50
    
urlpatterns = [
    url(r'^$', views.index),
    url(r'buy/(?P<item_id>)', views.buy),
    url(r'checkout$', views.checkout),
    
]

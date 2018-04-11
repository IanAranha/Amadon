
from django.conf.urls import url, include
from django.contrib import admin

def test(request):
    print '#' * 50
    print 'Project level good'
    print '@' * 50
    
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.amadon_app.urls'))
]

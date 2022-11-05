from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Members

# Create your views here.
def index(request):
    myclients = Members.objects.all().values()
    template = loader.get_template('clients.html')
    context = {
        'myclients': myclients,
    }

    return HttpResponse(template.render(context, request))
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    members = Members(firstname=x, lastname=y)
    members.save()
    return HttpResponseRedirect(reverse('index'))

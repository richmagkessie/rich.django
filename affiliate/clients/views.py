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

def delete(request, id):
    member = Members.objects.all().get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))

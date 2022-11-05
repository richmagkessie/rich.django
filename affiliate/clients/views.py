from django.template import loader
from django.http import HttpResponse
from .models import Members

# Create your views here.
def index(request):
    myclients = Members.objects.all().values()
    template = loader.get_template('clients.html')
    context = {
        'myclients': myclients,
    }
    return HttpResponse(template.render(context, request))

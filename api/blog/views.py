
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Poll, Choice ,Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from rest_framework import filters
from rest_framework import viewsets

# Create your views here.


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])



class PollViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer



###  Seeder

seeder = Seed.seeder()

Images = [os.path.join(settings.BASE_DIR,'static/images/breakfast-'+str(i)+'.jpg') for i in range(1,5)]+ [os.path.join(settings.BASE_DIR,'static/images/lunch-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dinner-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dessert-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/drink-'+str(i)+'.jpg') for i in range(1,6)]

def getimage()
    global Images
    img=images[randint(0,len(images)-1)]
    img = open(img,'rb')
    return img



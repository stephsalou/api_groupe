
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Poll, Choice ,Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from rest_framework import filters
from rest_framework import viewsets
from .models import *

# Create your views here.


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])



class PollViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer



###  Seeder

Images = [os.path.join(settings.BASE_DIR,'static/images/breakfast-'+str(i)+'.jpg') for i in range(1,5)]+ [os.path.join(settings.BASE_DIR,'static/images/lunch-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dinner-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dessert-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/drink-'+str(i)+'.jpg') for i in range(1,6)]

def getimage()
    global Images
    img=images[randint(0,len(images)-1)]
    img = open(img,'rb')
    return img


def basic_seeder():
    from django.core.files import File
    seeder = Seed.seeder()
    seeder.add_entity(Categorie, 10,{
        'image': File(getimage())
    })
    seeder.add_entity(User, 10)
    seeder.add_entity(SousCategorie, 30,{
        'image': File(getimage())
    })
    seeder.add_entity(Article, 50,{
        'image': File(getimage())
    })
    seeder.add_entity(Commentaire, 100)
    inserted_pks = seeder.execute()
from django.contrib.auth.models import User, Group # remove later on
from rest_framework import serializers
from complaints.models import Complaints,Villagename

class ComplaintsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complaints
       # fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'


class VillageNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villagename
        fields = '__all__'
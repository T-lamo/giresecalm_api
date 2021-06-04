
from re import S
from rest_framework import serializers
from ..my_models.ong import OngTb,BeneficiaireOngTb,BeneficiaireTb
from ..my_serializers.auth_user import AuthUserSerializer
from ..my_serializers.beneficiaire_ong import BeneficiaireOngTbSerializer
from ..my_serializers.temoignage import TemoignageSerializer
#from ..models import ong
class  BeneficiaireTbSerializer(serializers.ModelSerializer):
    beneficiaire_ong = BeneficiaireOngTbSerializer(many=True , read_only=True)
    temoignage=TemoignageSerializer(many=True, read_only=True)
    class Meta:
        model = BeneficiaireTb
        fields= ['firstname','nom','beneficiaire_ong','temoignage']
        #fields='__all__'

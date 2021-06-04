from re import S
from rest_framework import serializers
from ..my_models.ong import OngTb,BeneficiaireOngTb,BeneficiaireTb
from ..my_serializers.auth_user import AuthUserSerializer
from ..my_serializers.beneficiaire import BeneficiaireTbSerializer
from ..my_serializers.beneficiaire_ong import BeneficiaireOngTbSerializer
from ..my_serializers.beneficiaire import BeneficiaireOngTbSerializer
#from ..models import ong

class  OngTbSerializer(serializers.ModelSerializer):
    users = AuthUserSerializer(many=True , read_only=True)
    ong_beneficiaire = BeneficiaireOngTbSerializer(many=True , read_only=True)

    class Meta:
        model = OngTb
        #fields= ['id','content','author','post']
        fields=['nom', 'users','ong_beneficiaire']
    def __str__(self):
        return '%s' % ( self.libelle)



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    fonction = models.ForeignKey('FonctionTb', models.DO_NOTHING, blank=True, null=True)
    ong = models.ForeignKey('OngTb', models.DO_NOTHING, blank=True, null=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    telephone = models.TextField(blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class AvancementIndicateurTb(models.Model):
    avancement_indicateur_id = models.AutoField(primary_key=True)
    indicateur = models.ForeignKey('IndicateurTb', models.DO_NOTHING)
    realisation = models.FloatField()
    annee = models.DateField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'avancement_indicateur_tb'


class BassinVersantTb(models.Model):
    bassin_versant_id = models.IntegerField(primary_key=True)
    section_communale = models.ForeignKey('SectionCommunaleTb', models.DO_NOTHING)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bassin_versant_tb'


class BeneficiaireOngTb(models.Model):
    beneficiaire_ong_id = models.AutoField(primary_key=True)
    beneficiaire = models.ForeignKey('BeneficiaireTb', models.DO_NOTHING)
    ong = models.ForeignKey('OngTb', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'beneficiaire_ong_tb'


class BeneficiaireTb(models.Model):
    beneficiaire_id = models.AutoField(primary_key=True)
    localite = models.ForeignKey('LocaliteTb', models.DO_NOTHING)
    firstname = models.CharField(max_length=50)
    nom = models.CharField(max_length=255)
    prenom = models.DateField()
    cin = models.CharField(max_length=50, blank=True, null=True)
    sexe = models.CharField(max_length=10)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'beneficiaire_tb'


class CategorieIndicateur(models.Model):
    categorie_indicateur_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    valeur_representative = models.FloatField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categorie_indicateur'


class CommuneTb(models.Model):
    commune_id = models.AutoField(primary_key=True)
    departement = models.ForeignKey('DepartementTb', models.DO_NOTHING)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'commune_tb'


class DepartementTb(models.Model):
    departement_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'departement_tb'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExtrantTb(models.Model):
    extrant_id = models.AutoField(primary_key=True)
    categorie_indicateur = models.ForeignKey(CategorieIndicateur, models.DO_NOTHING)
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255)
    valeur_representative = models.FloatField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'extrant_tb'


class FonctionTb(models.Model):
    fonction_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    statut = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fonction_tb'


class HeiferBeneficiaire(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sexe = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'heifer_beneficiaire'


class ImpactTb(models.Model):
    impact_id = models.AutoField(primary_key=True)
    type_impact = models.ForeignKey('TypeImpactTb', models.DO_NOTHING)
    libelle = models.CharField(max_length=255)
    type = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'impact_tb'


class IndicateurOngTb(models.Model):
    indicateur_ong_id = models.AutoField(primary_key=True)
    indicateur = models.ForeignKey('IndicateurTb', models.DO_NOTHING)
    ong = models.ForeignKey('OngTb', models.DO_NOTHING)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indicateur_ong_tb'


class IndicateurResultatTb(models.Model):
    indicateur_resultat_id = models.AutoField(primary_key=True)
    categorie_indicateur = models.ForeignKey(CategorieIndicateur, models.DO_NOTHING)
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255)
    valeur_representative = models.FloatField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indicateur_resultat_tb'


class IndicateurTb(models.Model):
    indicateur_id = models.AutoField(primary_key=True)
    indicateur_resultat = models.ForeignKey(IndicateurResultatTb, models.DO_NOTHING, blank=True, null=True)
    sous_extrant = models.ForeignKey('SousExtrantTb', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255)
    cible = models.FloatField()
    valeur_base = models.FloatField()
    valeur_representative = models.FloatField()
    description = models.CharField(max_length=1000)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indicateur_tb'


class InfoUtilisateurTb(models.Model):
    info_utilisateur_id = models.AutoField(primary_key=True)
    user_auth_id = models.IntegerField()
    fonction = models.ForeignKey(FonctionTb, models.DO_NOTHING)
    ong_id = models.IntegerField()
    telephone = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'info_utilisateur_tb'


class LocaliteTb(models.Model):
    localite_id = models.AutoField(primary_key=True)
    bassin_versant = models.ForeignKey(BassinVersantTb, models.DO_NOTHING, blank=True, null=True)
    risque = models.ForeignKey('RisqueTb', models.DO_NOTHING)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'localite_tb'


class OngTb(models.Model):
    ong_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ong_tb'


class RisqueTb(models.Model):
    risque_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'risque_tb'


class SectionCommunaleTb(models.Model):
    section_communale_id = models.AutoField(primary_key=True)
    commune = models.ForeignKey(CommuneTb, models.DO_NOTHING)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'section_communale_tb'


class SousExtrantTb(models.Model):
    sous_extrant_id = models.AutoField(primary_key=True)
    extrant = models.ForeignKey(ExtrantTb, models.DO_NOTHING)
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255)
    valeur_representative = models.FloatField()
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sous_extrant_tb'


class SystemLogTb(models.Model):
    log_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'system_log_tb'


class Temoignage(models.Model):
    temoignage_id = models.AutoField(primary_key=True)
    beneficiaire = models.ForeignKey(BeneficiaireTb, models.DO_NOTHING)
    contenu = models.CharField(max_length=255)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'temoignage'


class TypeImpactTb(models.Model):
    type_impact_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_impact_tb'

# -*- coding: utf-8 -*-

from peewee import *

database = MySQLDatabase('netacad', **{'password': 'cisco', 'user': 'netacad', 'host': '10.60.21.3'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class AcademyGroup(BaseModel):
    id_academy_group = PrimaryKeyField()
    name_academy_group = CharField(null=True)

    class Meta:
        db_table = 'academy_group'

class Institution(BaseModel):
    addr1_institution = CharField(null=True)
    addr2_institution = CharField(null=True)
    city_institution = CharField(null=True)
    id_institution = PrimaryKeyField()
    latitude = FloatField()
    longitude = FloatField()
    name_institution = CharField(null=True)
    num_id_netacad = IntegerField(null=True)
    phone_institution = CharField(null=True)
    state_institution = CharField(null=True)
    zip_institution = CharField(null=True)

    class Meta:
        db_table = 'institution'

class Metrics(BaseModel):
    account_status_institution_role_attributes = CharField(null=True)
    bool_active_academy = CharField(null=True)
    bool_asc_cisco_academy = IntegerField(null=True)
    bool_cisco_academy = IntegerField(null=True)
    bool_itc_cisco_academy = IntegerField(null=True)
    ccna_fqtd = IntegerField(null=True)
    ccna_fytd = IntegerField(null=True)
    ccnas_fqtd = IntegerField(null=True)
    ccnas_fytd = IntegerField(null=True)
    ccnp_fqtd = IntegerField(null=True)
    ccnp_fytd = IntegerField(null=True)
    date_current_status_institution_role_attributes = CharField(null=True)
    date_resume = DateField(null=True)
    day_time = CharField(null=True)
    id_institution = ForeignKeyField(db_column='id_institution', rel_model=Institution, to_field='id_institution')
    id_metrics = PrimaryKeyField()
    institution_created_date_institution_role_attributes = CharField(null=True)
    ite_fqtd = IntegerField(null=True)
    ite_fytd = IntegerField(null=True)
    month_time = CharField(null=True)
    nb_student_ccna_security = IntegerField(null=True)
    nb_student_ccnp = IntegerField(null=True)
    nb_student_connecting_networks_ccna_routing_switching = IntegerField(null=True)
    nb_student_introduction_networks_ccna_routing_switching = IntegerField(null=True)
    nb_student_it_essential = IntegerField(null=True)
    nb_student_lvl_1_ccna_discovery = IntegerField(null=True)
    nb_student_lvl_1_ccna_exploration = IntegerField(null=True)
    nb_student_lvl_2_ccna_discovery = IntegerField(null=True)
    nb_student_lvl_2_ccna_exploration = IntegerField(null=True)
    nb_student_lvl_3_ccna_discovery = IntegerField(null=True)
    nb_student_lvl_3_ccna_exploration = IntegerField(null=True)
    nb_student_lvl_4_ccna_discovery = IntegerField(null=True)
    nb_student_lvl_4_ccna_exploration = IntegerField(null=True)
    nb_student_network_basic_ccna_routing_switching = IntegerField(null=True)
    nb_student_routing_protocols_ccna_routing_switching = IntegerField(null=True)
    nb_student_scaling_networks_ccna_routing_switching = IntegerField(null=True)
    nb_student_switched_networks_ccna_routing_switching = IntegerField(null=True)
    nb_student_switching_essentials_ccna_routing_switching = IntegerField(null=True)
    pass_ramp_up_rule_active_academy = CharField(null=True)
    passed_class_rule_active_academy = CharField(null=True)
    total_active_instructor = IntegerField(null=True)
    total_active_instructor_female = IntegerField(null=True)
    total_any_graduate_inception = IntegerField(null=True)
    total_any_graduate_inception_female = IntegerField(null=True)
    total_certification_ready_inception = IntegerField(null=True)
    total_certification_ready_inception_female = IntegerField(null=True)
    total_cumul_students_inception = IntegerField(null=True)
    total_cumul_students_inception_female = IntegerField(null=True)
    total_students = IntegerField(null=True)
    total_students_female = IntegerField(null=True)
    year_time = IntegerField(null=True)

    class Meta:
        db_table = 'metrics'

class Users(BaseModel):
    password = CharField()
    username = CharField()

    class Meta:
        db_table = 'users'

class VillesFrance(BaseModel):
    ville_amdi = IntegerField(null=True)
    ville_arrondissement = IntegerField(null=True)
    ville_canton = CharField(null=True)
    ville_code_commune = CharField(index=True)
    ville_code_postal = CharField(index=True, null=True)
    ville_commune = CharField(null=True)
    ville_densite_2010 = IntegerField(null=True)
    ville_departement = CharField(index=True, null=True)
    ville = PrimaryKeyField(db_column='ville_id')
    ville_latitude_deg = FloatField(null=True)
    ville_latitude_dms = CharField(null=True)
    ville_latitude_grd = CharField(null=True)
    ville_longitude_deg = FloatField(null=True)
    ville_longitude_dms = CharField(null=True)
    ville_longitude_grd = CharField(null=True)
    ville_nom = CharField(index=True, null=True)
    ville_nom_metaphone = CharField(index=True, null=True)
    ville_nom_reel = CharField(index=True, null=True)
    ville_nom_simple = CharField(index=True, null=True)
    ville_nom_soundex = CharField(index=True, null=True)
    ville_population_1999 = IntegerField(null=True)
    ville_population_2010 = IntegerField(index=True, null=True)
    ville_population_2012 = IntegerField(null=True)
    ville_slug = CharField(null=True)
    ville_surface = FloatField(null=True)
    ville_zmax = IntegerField(null=True)
    ville_zmin = IntegerField(null=True)

    class Meta:
        db_table = 'villes_france'



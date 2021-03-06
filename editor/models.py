# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Varsinaissuomenpalvelut(models.Model):
    gid = models.AutoField(primary_key=True)
    kohde = models.CharField(max_length=50, blank=True, null=True)
    postinumer = models.CharField(max_length=254, blank=True, null=True)
    kunta = models.CharField(max_length=254, blank=True, null=True)
    nimi = models.CharField(max_length=254, blank=True, null=True)
    aukiolo = models.CharField(max_length=50, blank=True, null=True)
    kunta_2011 = models.CharField(max_length=254, blank=True, null=True)
    lis_tiedot = models.CharField(db_column='lis\xe4tiedot', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    katuosoite = models.CharField(max_length=254, blank=True, null=True)
    kuntanro = models.IntegerField(blank=True, null=True)
    kohdenro = models.IntegerField(blank=True, null=True)
    paikkaluku = models.IntegerField(blank=True, null=True)
    julkpalvel = models.CharField(max_length=10, blank=True, null=True)
    wwwlinkki = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    paivittaja = models.CharField(max_length=50, blank=True, null=True)
    puhelin = models.CharField(max_length=15, blank=True, null=True)
    visual = models.CharField(max_length=250, blank=True, null=True)
    legend = models.CharField(max_length=250, blank=True, null=True)
    postinro = models.CharField(max_length=5, blank=True, null=True)
    kohde2 = models.CharField(max_length=80, blank=True, null=True)
    geom = models.PointField(srid=3067, dim=4, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'varsinaissuomenpalvelut'

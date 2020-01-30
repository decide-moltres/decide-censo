from django.contrib import admin
from django.shortcuts import redirect, render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.status import (
        HTTP_201_CREATED as ST_201,
        HTTP_204_NO_CONTENT as ST_204,
        HTTP_400_BAD_REQUEST as ST_400,
        HTTP_401_UNAUTHORIZED as ST_401,
        HTTP_409_CONFLICT as ST_409
)

from .models import Census
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from voting.models import Voting
from django.contrib.auth.models import User

import psycopg2
import xlsxwriter

def export_census(modeladmin, request, queryset):
    con = psycopg2.connect(database="postgres", user="decide", password="decide", host="127.0.0.1", port="5432")
    print("Database opened successfully")
    cur = con.cursor()
    cur2 = con.cursor()


    cur.execute("SELECT * FROM census_census")
    cur2.execute("SELECT * FROM census_census_voter_id")
    n = cur.fetchall()
    n2 = cur2.fetchall()
    workbook = xlsxwriter.Workbook('Decide_census.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "census_id")
    worksheet.write(0, 1, "voting_id")
    worksheet.write(0, 2, "voters_id")
    row = 1
    col = 0
    p = []
    for item in n:
        for item2 in n2:
            if item2[1]==item[0]:
                p.append(item2[2])
        worksheet.write(row, col, str(item[0]))
        worksheet.write(row, col + 1, str(item[1]))
        worksheet.write(row, col + 2, str(p))
        p = []
        row += 1

    print(n)
    workbook.close()


class CensusResource(resources.ModelResource):
    class Meta:
        model= Census


def viewVoters(modeladmin, request, queryset, *voting_id):

    voter = request.GET.get('voter_id')
    #voter = Voter.objects.all()
    #voters = Census.objects.get(voter_id=voter)
    users = User.objects.all()
    census = set(Census.objects.filter(voting_id=request.GET.get('voting_id')))

    for censo in census:

        usuario = Census.objects.filter(voting_id=voting_id).values_list('voter_id', flat=True)
        users.append(usuario)

    return render(request, "view_voters.html", {'users': users})    
# def corrector_nombres(modeladmin, request, queryset):

#     #Me traigo todos los censos
#     con = psycopg2.connect(database="postgres", user="decide", password="decide", host="127.0.0.1", port="5432")
#     print("Database opened successfully")
#     cur = con.cursor()

#     cur.execute("SELECT * FROM census_census");
#     n = cur.fetchall()
#     print("Census")
#     print(n)

#     #Lista de palabras malas:
#     palabras = ["fuck", "bitch", "stupid"]

#     for e in n:
#         id = e[0] #Hay que revisar esto tras el cambio de modelo, despues debe funcionar
#         print(id)
#         #Obtengo el objeto
#         obj = Census.objects.get(pk=id)
#         #Cuando pueda probar, mirar que puedo cambiar el nombre y guardarlo

#         #Miro que su nombre no este en la lista mala
#         nombre = obj.name()
#         if nombre in lista_palabras_malas:
#             new_name = "nombre "
#             new_name = new_name + obj.voting_id
#             obj.name = new_name
#             obj.save()


class CensusAdmin(admin.ModelAdmin):
    list_display = ('name', 'voting_id')
    list_filter = ('name', 'voting_id')

    search_fields = ('voter_id', )

    actions = [ export_census, viewVoters ]

    object_edit_template = "edit_census.html"
    object_delete_template = "delete_census.html"
    object_history_template = "census_history.html"



admin.site.register(Census, CensusAdmin)

from django.contrib import admin

from .models import Census

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
        s = ""
        worksheet.write(row, col + 2, str(p))
        p = []
        row += 1
       
    print(n)
    workbook.close()


# def import_census(modeladmin, request, queryset):
    

#     conn = psycopg2.connect(database="postgres", user="decide", password="decide", host="127.0.0.1", port="5432") 
#     cur = conn.cursor()

#     # creamos la tabla
#     cur.execute('''create table test(census_id char(50), voting_id char(50), voters_id char(50));''')

   
#     # copiamos lo de file.csv a la base de datos
#     f = open('file.csv','r')
#     cur.copy_from(f, 'test', sep=',')
#     f.close()

class CensusAdmin(admin.ModelAdmin):
    list_display = ('voting_id', )
    list_filter = ('voting_id', )

    search_fields = ('voter_id', )

    actions = [ export_census,
    #  import_census
     ]


admin.site.register(Census, CensusAdmin)

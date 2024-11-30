from django.contrib import admin
from .models import Curso




admin.site.site_header = "Painel Admin DevMaster"
admin.site.site_title = "Portal DevMaster Admin"
admin.site.index_title = "Bem-vindo ao Portal DevMaster Admin"


admin.site.register(Curso)

from django.contrib import admin
from .models import estado, matricula, leiloeiro, anexo

admin.site.register(leiloeiro)
admin.site.register(matricula)
admin.site.register(estado)
admin.site.register(anexo)

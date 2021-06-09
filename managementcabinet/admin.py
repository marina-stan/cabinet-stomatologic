from django.contrib import admin
from .models import Medic
from .models import Asistent
from .models import Pacient

admin.site.register(Medic)
admin.site.register(Asistent)
admin.site.register(Pacient)

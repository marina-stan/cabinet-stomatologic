from django.contrib import admin
from .models import Medic
from .models import Asistent
from .models import Pacient
from .models import Programare
from .models import Consultatie
from .models import Diagnostic
from .models import Partener
from .models import Produs
from .models import Tratament
from .models import Factura
from .models import FisaPacient


admin.site.register(Medic)
admin.site.register(Asistent)
admin.site.register(Pacient)
admin.site.register(Programare)
admin.site.register(Consultatie)
admin.site.register(Diagnostic)
admin.site.register(Partener)
admin.site.register(Produs)
admin.site.register(Tratament)
admin.site.register(Factura)
admin.site.register(FisaPacient)

from django.contrib import admin
from .models import Marmot, Feeding, Toy

# Register your models here.
admin.site.register(Marmot)
admin.site.register(Feeding)
admin.site.register(Toy)
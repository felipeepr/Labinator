from django.contrib import admin

from .models import Samples
from .models import Result

admin.site.register(Samples)
admin.site.register(Result)

from django.contrib import admin
from newsletter.models import NewsLetter

# Register your models here.

class NewsLetterAdmin(admin.ModelAdmin):
	fieldsets = [	
		('first_name',	{'fields': ['First Name']}),
		('last_name',	{'fields': ['Last Name']}),
		('email_field',	{'fields': ['Email']}),
	]

admin.site.register(NewsLetter, NewsLetterAdmin)
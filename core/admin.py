from django.contrib import admin
from models import Job, Category

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
admin.site.register(Job)
admin.site.register(Category, CategoryAdmin)

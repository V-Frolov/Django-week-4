from django.contrib import admin
from .models import Authors, Books, Member, Profile, Reviews


admin.site.register(Authors)
admin.site.register(Member)
admin.site.register(Profile)
admin.site.register(Reviews)


class BooksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Books._meta.fields]
    search_fields = ['id', 'title', 'description']
    list_filter = ['id', 'title', 'description']
    list_editable = ('title',)

    class Meta:
        model = Books


admin.site.register(Books, BooksAdmin)

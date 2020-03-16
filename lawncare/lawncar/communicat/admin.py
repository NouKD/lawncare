from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.CategorieArticle)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.Commentaire)
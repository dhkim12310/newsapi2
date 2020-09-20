from django.contrib  import admin
from news.api.models import Article, Journalist

admin.site.register(Article)
admin.site.register(Journalist)
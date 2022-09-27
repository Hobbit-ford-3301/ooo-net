from django.contrib import admin

from .models import Article, ArticleScope, Tag


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass
from django.contrib import admin

from .models import Category, Item, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    name_name = Item.name.field.name
    is_published_name = Item.is_published.field.name
    tags_name = Item.tags.field.name

    list_display = (
        name_name,
        is_published_name,
    )
    list_editable = (is_published_name,)
    list_display_links = (name_name,)
    filter_horizontal = (tags_name,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    name_name = Tag.name.field.name
    slug = Tag.slug.field.name

    prepopulated_fields = {slug: (name_name,)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    name_name = Category.name.field.name
    slug = Category.slug.field.name

    prepopulated_fields = {slug: (name_name,)}

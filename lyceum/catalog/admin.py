import catalog.models

import django.contrib.admin


@django.contrib.admin.register(catalog.models.Item)
class ItemAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)


@django.contrib.admin.register(catalog.models.Tag)
class TagAdmin(django.contrib.admin.ModelAdmin):
    prepopulated_fields = {
        catalog.models.Tag.slug.field.name: (
            catalog.models.Tag.name.field.name,
        )
    }


@django.contrib.admin.register(catalog.models.Category)
class CategoryAdmin(django.contrib.admin.ModelAdmin):
    prepopulated_fields = {
        catalog.models.Category.slug.field.name: (
            catalog.models.Category.name.field.name,
        )
    }

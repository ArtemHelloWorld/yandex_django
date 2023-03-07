import catalog.models
import django.contrib.admin
import django.db.models
import tinymce.widgets


class ImageGalleryInline(django.contrib.admin.StackedInline):
    model = catalog.models.ItemImageGallery
    extra = 1


@django.contrib.admin.register(catalog.models.Item)
class ItemAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.date_created.field.name,
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.is_on_main.field.name,
    )
    list_editable = (
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.is_on_main.field.name,
    )
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)

    formfield_overrides = {
        django.db.models.TextField: {"widget": tinymce.widgets.TinyMCE},
    }

    inlines = [
        ImageGalleryInline,
    ]


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


django.contrib.admin.site.register(catalog.models.ItemImageMain)
django.contrib.admin.site.register(catalog.models.ItemImageGallery)

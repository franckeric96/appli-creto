from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from Action.action import Action


class ProduitInline(admin.TabularInline):
    model = models.Produit
    extra = 1


class CategorieAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update',
                    'status', 'images_view')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Categorie', {'fields': ['nom', 'description', 'image']}),
                 ('Standare', {'fields': ['status']})
                 ]
    inlines = [ProduitInline]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class PanierAdmin(Action):
    list_display = ('images_view', 'produit', 'quantite', 'date_add', 'date_update', 'status')
    list_filter = ('status', )
    search_fields = ('produit', )
    date_hierarchy = 'date_add'
    list_display_links = ['produit']
    ordering = ['date_update']
    list_per_page = 10
    fieldsets = [('Info Panier', {'fields': ['produit', 'quantite']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:80px; width:80px">'.format(url=obj.produit.image.url))


class ProduitAdmin(Action):
    list_display = ('nom', 'prix', 'categorie', 'date_add', 'date_update',
                    'status', 'images_view')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Produit', {'fields': ['nom', 'prix', 'description', 'image', 'categorie']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Produit, ProduitAdmin)
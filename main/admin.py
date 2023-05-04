from django.contrib import admin

from .models import *  # Application, Welding_method, Aplic_status, Weld_select

# Register your models here.


#
@admin.register(Material_Flux)
class Material_FluxAdmin(admin.ModelAdmin):
    list_display = ("brand",)


@admin.register(Material_Wire)
class Material_WireAdmin(admin.ModelAdmin):
    list_display = ("brand", "diameter")


@admin.register(Material_Rod)
class Material_RodAdmin(admin.ModelAdmin):
    list_display = ("brand", "diameter")


@admin.register(Material_Electrode)
class Material_ElectrodeAdmin(admin.ModelAdmin):
    list_display = ("brand", "diameter")


@admin.register(Material_Tube)
class Material_TubeAdmin(admin.ModelAdmin):
    list_display = (
        "diameter",
        "thickness",
        "group_of_material",
        "steel_grade")


@admin.register(Material_Plate)
class Material_PlateAdmin(admin.ModelAdmin):
    list_display = ("thickness", "group_of_material", "steel_grade")


@admin.register(Welding_method)
class Welding_methodAdmin(admin.ModelAdmin):
    list_display = (
        "weld_des",
        "weld_short",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("aplic_date",)


# Aplic_status


@admin.register(Aplic_status)
class Aplic_statusAdmin(admin.ModelAdmin):
    list_display = ("aplic_name",)


@admin.register(Weld_select)
class Weld_selectAdmin(admin.ModelAdmin):
    list_display = ("select_name",)

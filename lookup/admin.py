from django.contrib import admin

from .models import *


class est_typeAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(est_typeAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['created_by'].initial = request.user
        form.base_fields['created_by'].disabled = True
        form.base_fields['created_by'].help_text = "This field is set to current_user and it's not editable"
        form.base_fields['updated_by'].initial = request.user
        form.base_fields['updated_by'].disabled = True
        form.base_fields['updated_by'].help_text = "This field is set to current_user and it's not editable"
        return form


class sexAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(sexAdmin, self).get_form(request, obj, **kwargs)
        return form


class identity_typeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(identity_typeAdmin, self).get_form(request, obj, **kwargs)
        return form


class titleAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(titleAdmin, self).get_form(request, obj, **kwargs)
        return form


class tribeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(tribeAdmin, self).get_form(request, obj, **kwargs)
        return form


class nationalityAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(nationalityAdmin, self).get_form(request, obj, **kwargs)
        return form


class education_levelAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(education_levelAdmin, self).get_form(request, obj, **kwargs)
        return form


class next_of_kin_typeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(next_of_kin_typeAdmin, self).get_form(request, obj, **kwargs)
        return form


class animal_typeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(animal_typeAdmin, self).get_form(request, obj, **kwargs)
        return form


class statusAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(statusAdmin, self).get_form(request, obj, **kwargs)
        return form


class originAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(originAdmin, self).get_form(request, obj, **kwargs)
        return form


class dom_skin_colorAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(dom_skin_colorAdmin, self).get_form(request, obj, **kwargs)
        return form


class breedAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(breedAdmin, self).get_form(request, obj, **kwargs)
        return form


class tag_statusAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(tag_statusAdmin, self).get_form(request, obj, **kwargs)
        return form


class operation_statusAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(operation_statusAdmin, self).get_form(request, obj, **kwargs)
        return form


class incident_priority_levelAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(incident_priority_levelAdmin, self).get_form(request, obj, **kwargs)
        return form


class incident_typeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(incident_typeAdmin, self).get_form(request, obj, **kwargs)
        return form


class transfer_statusAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(transfer_statusAdmin, self).get_form(request, obj, **kwargs)
        return form


class transit_categoryAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(transit_categoryAdmin, self).get_form(request, obj, **kwargs)
        return form


class vehicle_makeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(vehicle_makeAdmin, self).get_form(request, obj, **kwargs)
        return form


class vehicle_modelAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(vehicle_modelAdmin, self).get_form(request, obj, **kwargs)
        return form


class transfer_fee_typeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(transfer_fee_typeAdmin, self).get_form(request, obj, **kwargs)
        return form


class payment_modeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(payment_modeAdmin, self).get_form(request, obj, **kwargs)
        return form


class payment_channelAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(payment_channelAdmin, self).get_form(request, obj, **kwargs)
        return form


class quarantine_statusAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(quarantine_statusAdmin, self).get_form(request, obj, **kwargs)
        return form


class quarantine_reasonAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(quarantine_reasonAdmin, self).get_form(request, obj, **kwargs)
        return form


class transfer_action_typeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(transfer_action_typeAdmin, self).get_form(request, obj, **kwargs)
        return form


class mode_of_transportAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(mode_of_transportAdmin, self).get_form(request, obj, **kwargs)
        return form


class animal_action_typeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(animal_action_typeAdmin, self).get_form(request, obj, **kwargs)
        return form


class ownership_change_typeAdmin(est_typeAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(ownership_change_typeAdmin, self).get_form(request, obj, **kwargs)
        return form


admin.site.register(est_type, est_typeAdmin)
admin.site.register(sex, sexAdmin)
admin.site.register(identity_doc_type, identity_typeAdmin)
admin.site.register(title, titleAdmin)
admin.site.register(tribe, tribeAdmin)
admin.site.register(nationality, nationalityAdmin)
admin.site.register(education_level, education_levelAdmin)
admin.site.register(next_of_kin_type, next_of_kin_typeAdmin)
admin.site.register(animal_type, animal_typeAdmin)
admin.site.register(breed, breedAdmin)
admin.site.register(dom_skin_color, dom_skin_colorAdmin)
admin.site.register(origin, originAdmin)
admin.site.register(status, statusAdmin)
admin.site.register(tag_status, tag_statusAdmin)
admin.site.register(incident_type, incident_typeAdmin)
admin.site.register(incident_priority_level, incident_priority_levelAdmin)
admin.site.register(operation_status, operation_statusAdmin)
admin.site.register(transfer_status, transfer_statusAdmin)
admin.site.register(transit_category, transit_categoryAdmin)
admin.site.register(vehicle_make, vehicle_makeAdmin)
admin.site.register(vehicle_model, vehicle_modelAdmin)
admin.site.register(transfer_fee_type, transfer_fee_typeAdmin)
admin.site.register(payment_mode, payment_modeAdmin)
admin.site.register(payment_channel, payment_modeAdmin)
admin.site.register(quarantine_status, quarantine_statusAdmin)
admin.site.register(quarantine_reason, quarantine_reasonAdmin)
admin.site.register(transfer_action_type, transfer_action_typeAdmin)
admin.site.register(mode_of_transport, mode_of_transportAdmin)
admin.site.register(animal_action_type, animal_action_typeAdmin)
admin.site.register(ownership_change_type, ownership_change_typeAdmin)

from django.contrib import admin
from .models import Project, Variable, Request


class VariableAdmin(admin.ModelAdmin):
    """
    This admin function is for setup the list view for variables table
    """
    list_display = (
        'name',
        'project',
        'description',
        'collected_datetime',
        'availability',
        'expiration_date'
    )
    list_filter = ('project',)
    search_fields = ('name', 'project__name', 'description')


class RequestAdmin(admin.ModelAdmin):
    """
    This admin function is for setup the view for the request table
    """
    list_display = (
        'id', 'get_requested_variables', 'user', 'get_reviewers', 'approved'
    )
    list_filter = ('approved',)

    def get_requested_variables(self, obj):
        return ", ".join(
            [variable.name for variable in obj.selected_variables.all()])

    get_requested_variables.short_description = 'Requested Variables'

    def get_reviewers(self, obj):
        return ", ".join(
            [reviewer.username for reviewer in obj.reviewers.all()])

    get_reviewers.short_description = 'Reviewers'


# Register the model into django admin
admin.site.register(Variable, VariableAdmin)
admin.site.register(Project)
admin.site.register(Request, RequestAdmin)

from django.contrib import admin
from .models import Project, Variable, Request


class VariableAdmin(admin.ModelAdmin):
    """
    This admin function is for setup the list view for variables table
    """

    list_display = (
        "name",
        "description",
        "collected_datetime",
        "availability",
        "expiration_date",
    )
    search_fields = ("name", "description")

    def request_ids(self, obj):
        return ", ".join([str(req) for req in obj.requests.all()])

    request_ids.short_description = "Request IDs"


class RequestAdmin(admin.ModelAdmin):
    list_display = ("request_id", "status", "username", "contact_email")
    list_filter = ("status",)

    # pre-select the requested variables in the Django admin
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        if "_changelist_filters" in request.GET:
            return initial

        # Get the object ID from the URL
        obj_id = request.resolver_match.args[0]
        try:
            obj = self.get_queryset(request).get(pk=obj_id)
            initial["variables"] = obj.variables.all()
        except Request.DoesNotExist:
            pass

        return initial

    def request_ids(self, obj):
        return ", ".join([str(req) for req in obj.request_set.all()])

    request_ids.short_description = "Request IDs"


# Register the model into django admin
admin.site.register(Variable, VariableAdmin)
admin.site.register(Project)
admin.site.register(Request, RequestAdmin)

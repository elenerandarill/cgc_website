from django.contrib import admin
from .models import TeamMember, TeamMemberTrans, CommonText, CommonTextTrans, ClientLogo, ServicesItem, ServicesItemTrans, WorkflowItem, WorkflowItemTrans


class CommonTextInline(admin.TabularInline):
    model = CommonTextTrans


class CommonTextAdmin(admin.ModelAdmin):
    inlines = [CommonTextInline]


class WorkflowItemTransInline(admin.TabularInline):
    model = WorkflowItemTrans


class WorkflowItemAdmin(admin.ModelAdmin):
    inlines = [WorkflowItemTransInline]


class TeamMemberTransInline(admin.TabularInline):
    model = TeamMemberTrans


class TeamMemberAdmin(admin.ModelAdmin):
    inlines = [TeamMemberTransInline]


class ServicesItemTransInline(admin.TabularInline):
    model = ServicesItemTrans


class ServicesItemAdmin(admin.ModelAdmin):
    inlines = [ServicesItemTransInline]


# Register your models here.

admin.site.register(CommonText, CommonTextAdmin)
admin.site.register(CommonTextTrans)

admin.site.register(WorkflowItem, WorkflowItemAdmin)
admin.site.register(WorkflowItemTrans)

admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(TeamMemberTrans)

admin.site.register(ServicesItem, ServicesItemAdmin)
admin.site.register(ServicesItemTrans)

admin.site.register(ClientLogo)



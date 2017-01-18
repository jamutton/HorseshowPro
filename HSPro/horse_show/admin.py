from horse_show.models import *
from django.contrib import admin

#######
# THIS IS A LEGACY FILE
# @TODO: Need to figure out exactly what is still used in here and/or drop the file

#CUSTOM ADMIN ACTIONS
#Classes
def make_medals_qual(modeladmin, request, queryset):
    queryset.update(isMedalsQualifying=True)
make_medals_qual.short_description = "Make all selected entries qualifying for medals"
def make_medals_not_qual(modeladmin, request, queryset):
    queryset.update(isMedalsQualifying=False)
make_medals_not_qual.short_description = "Make all selected entries NOT qualify for medals"
def make_state_qual(modeladmin, request, queryset):
    queryset.update(isStateQualifying=True)
make_state_qual.short_description = "Make all selected entries qualifying for state"
def make_state_not_qual(modeladmin, request, queryset):
    queryset.update(isStateQualifying=False)
make_state_not_qual.short_description = "Make all selected entries NOT qualify for state"
def make_hipoint(modeladmin, request, queryset):
    queryset.update(isHighpoint=True)
make_hipoint.short_description = "Make all selected entries count toward highpoint"
def make_not_hipoint(modeladmin, request, queryset):
    queryset.update(isHighpoint=False)
make_not_hipoint.short_description = "Make all selected entries NOT count toward highpoint"

# Riders
def make_not_novice(modeladmin, request, queryset):
    queryset.update(Novice=False)
make_not_novice.short_description = "Make all selected riders NOT Novice"
def make_novice(modeladmin, request, queryset):
    queryset.update(Novice=True)
make_novice.short_description = "Make all selected riders Novice"


#INLINES
class ClassEntryInline(admin.TabularInline):
	model = ClassEntry
	extra = 24
class ShowClassInline(admin.StackedInline):
	model = ShowClass
	extra = 10
class NumberInline(admin.TabularInline):
	model = Number
	extra = 5

#ADMINS
class RiderAdmin(admin.ModelAdmin):
	list_display = ('LastName', 'FirstName', 'Club', 'Division', 'Novice', 'HighpointTeam')
	list_filter = ['Club','Division']
	ordering = ('LastName','FirstName')
	search_fields = ['LastName','FirstName']
	fieldsets = [
        (None,               {'fields': ['LastName','FirstName','MiddleInitial','Division',]}),
        ('Additional Info', {'fields': ['Club','HighpointTeam','Novice','Grade','Birthday'], 'classes': ['collapse']}),
		('Communication', {'fields': ['EmailAddress','StreetAddress','City','MailRegion','PostalCode'], 'classes': ['collapse']})
    ]
	inlines = [NumberInline]
	actions = [make_novice,make_not_novice]
class JudgingAdmin(admin.ModelAdmin):
	list_display = ('Number','Show','ShowClass','Place','Danish','Point','Comments')
	list_filter = ['Show','ShowClass',]
	ordering = ('Show','Number','ShowClass')
	search_fields = ['Number']
class ShowAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Date')
class ShowClassAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Seat', 'isHighpoint', 'isMedalsQualifying', 'isStateQualifying',)
	actions = [make_medals_qual,make_medals_not_qual,make_state_qual,make_state_not_qual,make_hipoint,make_not_hipoint]
class EntryAdmin(admin.ModelAdmin):
	list_display = ('Number', 'Show')
	inlines = [ClassEntryInline]
	list_filter = ['Show']
class ShowClassScheduleAdmin(admin.ModelAdmin):
	list_display = ('ShowPosition', 'ShowClass', 'Show')
	list_filter = ['Show']
class ExtraFeeAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Cost', 'Default')
class HighpointPlacingAdmin(admin.ModelAdmin):
	list_display = ('Place', 'Points')
class LocationAdmin(admin.ModelAdmin):
	list_display = ('Name', 'City')

#REGISTRATION
admin.site.register(Club)
admin.site.register(Seat)
#admin.site.register(EntryType)
admin.site.register(Danish)
admin.site.register(Judge)
admin.site.register(Rider, RiderAdmin)
admin.site.register(HighpointTeam)
admin.site.register(Show, ShowAdmin)
admin.site.register(ShowClass, ShowClassAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(ShowClassSchedule, ShowClassScheduleAdmin)
#admin.site.register(ExtraFee, ExtraFeeAdmin)
admin.site.register(HighpointPlacing, HighpointPlacingAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Judging, JudgingAdmin)

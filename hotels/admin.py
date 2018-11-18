from django.contrib import admin

from .models import (Company, CompanyAdmin,
                     Hotel, HotelAdmin,
                     Floor, FloorAdmin,
                     Building, BuildingAdmin,
                     RoomType, RoomTypeAdmin,
                     Room, RoomAdmin,
                     RoleType,
                     PageSection)

# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoleType)
admin.site.register(PageSection)

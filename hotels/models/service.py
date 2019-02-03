##
#     Project: Django Hotels
# Description: A Django application to organize Hotels and Inns
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import collections

from django.db import models

from utility.models import BaseModel, BaseModelAdmin


class Service(BaseModel):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    room_service = models.BooleanField(default=False)
    extra_service = models.BooleanField(default=False)

    class Meta:
        # Define the database table
        db_table = 'hotels_services'
        ordering = ['name']

    def __str__(self):
        return self.name


class ServiceAdmin(BaseModelAdmin):
    list_display = ('name', 'description', 'room_service', 'extra_service')
    actions = ('action_export_csv', )
    # Define fields and attributes to export rows to CSV
    export_csv_fields_map = collections.OrderedDict({
        'NAME': 'name',
        'DESCRIPTION': 'description',
        'ROOM SERVICE': 'room_service',
    })

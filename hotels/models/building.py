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


class Building(BaseModel):

    structure = models.ForeignKey('Structure',
                                  on_delete=models.PROTECT,
                                  default=0)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    location = models.ForeignKey('locations.Location',
                                 on_delete=models.PROTECT,
                                 default=0)
    postal_code = models.CharField(max_length=15, blank=True)
    phone1 = models.CharField(max_length=255, blank=True)
    phone2 = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    class Meta:
        # Define the database table
        db_table = 'hotels_buildings'
        ordering = ['structure', 'name']
        unique_together = ('name', )

    def __str__(self):
        return self.name


class BuildingAdmin(BaseModelAdmin):
    list_filter = ('structure__company', 'structure')
    # Define fields and attributes to export rows to CSV
    export_csv_fields_map = collections.OrderedDict({
        'STRUCTURE': 'structure',
        'NAME': 'name',
        'DESCRIPTION': 'description',
        'ADDRESS': 'address',
        'LOCATION': 'location',
        'POSTAL CODE': 'postal_code',
        'PHONE1': 'phone1',
        'PHONE2': 'phone2',
        'FAX': 'fax',
        'EMAIL': 'email',
    })

    def brand(self, instance):
        return instance.structure.brand
    brand.short_description = 'Brand'

    def company(self, instance):
        return instance.structure.company
    company.short_description = 'Company'

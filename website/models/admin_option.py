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

from django.db import models

from utility.models import BaseModel, BaseModelAdmin


class AdminOption(BaseModel):

    section = models.CharField(max_length=255)
    group = models.CharField(max_length=255, default='main')
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    value = models.TextField(blank=True)

    class Meta:
        # Define the database table
        db_table = 'website_admin_options'
        ordering = ['section', 'group', 'name']
        unique_together = ('section', 'group', 'name')

    def __str__(self):
        return '{SECTION} - {GROUP} - {NAME}'.format(SECTION=self.section,
                                                     GROUP=self.group,
                                                     NAME=self.name)


class AdminOptionAdmin(BaseModelAdmin):
    pass
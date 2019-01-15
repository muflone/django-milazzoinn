##
#     Project: Django Milazzo Inn
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
from django.contrib import admin

from . import activity_room
from .contract import Contract
from .timestamp import Timestamp

from utility.admin_actions import ExportCSVMixin


class Activity(models.Model):

    contract = models.ForeignKey('Contract',
                                 on_delete=models.PROTECT)
    date = models.DateField()
    timestamps = models.ManyToManyField(Timestamp,
                                        db_table='work_activity_timestamps',
                                        blank=True)

    class Meta:
        # Define the database table
        db_table = 'work_activities'
        ordering = ['contract', 'date']
        verbose_name_plural = 'Activities'
        unique_together = ('contract', 'date')

    def __str__(self):
        return '{CONTRACT} {DATE}'.format(
            CONTRACT=self.contract,
            DATE=self.date)


class ActivityAdmin(admin.ModelAdmin, ExportCSVMixin):
    list_display = ('contract', 'date')
    actions = ('action_export_csv', )
    date_hierarchy = 'date'
    # Define fields and attributes to export rows to CSV
    export_csv_fields_map = collections.OrderedDict({
        'CONTRACT': 'contract',
        'DATE': 'date',
    })

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'timestamps':
            # Optimize value lookup for field timestamps
            if 'object_id' in request.resolver_match.kwargs:
                object_id = request.resolver_match.kwargs['object_id']
                instance = Activity.objects.get(pk=object_id)
                queryset = Timestamp.objects.filter(
                    contract_id=instance.contract_id,
                    date=instance.date)
            else:
                # During empty adding set no timestamp limit
                queryset = Timestamp.objects.all()
            kwargs['queryset'] = queryset.order_by('-date').select_related(
                'contract', 'contract__company', 'contract__employee')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'contract':
            # Optimize value lookup for field contract
            kwargs['queryset'] = Contract.objects.all().select_related(
                'employee', 'company')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ActivityInLinesProxy(Activity):
    class Meta:
        verbose_name_plural = 'Activities with Rooms'
        proxy = True


class ActivityInLinesAdmin(admin.ModelAdmin, ExportCSVMixin):
    list_display = ('contract', 'date')
    inlines = [activity_room.ActivityRoomInline, ]
    date_hierarchy = 'date'

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'timestamps':
            # Optimize value lookup for field timestamps
            if 'object_id' in request.resolver_match.kwargs:
                object_id = request.resolver_match.kwargs['object_id']
                instance = Activity.objects.get(pk=object_id)
                queryset = Timestamp.objects.filter(
                    contract_id=instance.contract_id,
                    date=instance.date)
            else:
                # During empty adding set no timestamp limit
                queryset = Timestamp.objects.all()
            kwargs['queryset'] = queryset.order_by('-date').select_related(
                'contract', 'contract__company', 'contract__employee')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'contract':
            # Optimize value lookup for field contract
            kwargs['queryset'] = Contract.objects.all().select_related(
                'employee', 'company')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

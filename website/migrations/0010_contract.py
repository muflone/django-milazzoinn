# Generated by Django 2.1.4 on 2018-12-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_contracttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminsearchable',
            name='model',
            field=models.CharField(choices=[('BedTypeAdmin', 'BedTypeAdmin'), ('BrandAdmin', 'BrandAdmin'), ('BuildingAdmin', 'BuildingAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('ContinentAdmin', 'ContinentAdmin'), ('ContractAdmin', 'ContractAdmin'), ('ContractTypeAdmin', 'ContractTypeAdmin'), ('CountryAdmin', 'CountryAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('JobTypeAdmin', 'JobTypeAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('LocationAdmin', 'LocationAdmin'), ('PositionAdmin', 'PositionAdmin'), ('RegionAdmin', 'RegionAdmin'), ('RegionAliasAdmin', 'RegionAliasAdmin'), ('RoomAdmin', 'RoomAdmin'), ('RoomTypeAdmin', 'RoomTypeAdmin'), ('StructureAdmin', 'StructureAdmin')], max_length=255),
        ),
        migrations.AlterField(
            model_name='adminsearchable',
            name='ref_model',
            field=models.CharField(choices=[('BedTypeAdmin', 'BedTypeAdmin'), ('BrandAdmin', 'BrandAdmin'), ('BuildingAdmin', 'BuildingAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('ContinentAdmin', 'ContinentAdmin'), ('ContractAdmin', 'ContractAdmin'), ('ContractTypeAdmin', 'ContractTypeAdmin'), ('CountryAdmin', 'CountryAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('JobTypeAdmin', 'JobTypeAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('LocationAdmin', 'LocationAdmin'), ('PositionAdmin', 'PositionAdmin'), ('RegionAdmin', 'RegionAdmin'), ('RegionAliasAdmin', 'RegionAliasAdmin'), ('RoomAdmin', 'RoomAdmin'), ('RoomTypeAdmin', 'RoomTypeAdmin'), ('StructureAdmin', 'StructureAdmin')], max_length=255),
        ),
    ]

# Generated by Django 2.1.5 on 2020-09-03 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, help_text='null表示不是菜单;非null表示是二级菜单', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rbac.Menu', verbose_name='所属菜单'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='pid',
            field=models.ForeignKey(blank=True, help_text='对于非菜单权限需要选择一个可以成为菜单的权限，用户做默认展开和选中菜单', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parents', to='rbac.Permission', verbose_name='关联的权限'),
        ),
    ]

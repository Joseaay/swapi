# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_editablemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='homeworld',
            new_name='planets',
        ),
        migrations.RenameField(
            model_name='species',
            old_name='homeworld',
            new_name='planets',
        ),
    ]

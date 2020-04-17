# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20200417_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='characters',
            new_name='people',
        ),
    ]

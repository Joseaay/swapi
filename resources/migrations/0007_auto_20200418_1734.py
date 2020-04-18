# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20200417_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='starship',
            old_name='pilots',
            new_name='people',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='pilots',
            new_name='people',
        ),
    ]

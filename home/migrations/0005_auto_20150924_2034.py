# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_lookbookpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lookbookpage',
            name='page_content',
        ),
        migrations.AddField(
            model_name='lookbookpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('lookbookimage', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)))), icon='image', template='home/blocks/image_holder.html'))), null=True, blank=True),
        ),
    ]

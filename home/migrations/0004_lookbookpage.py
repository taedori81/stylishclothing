# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('home', '0003_shoppage'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookbookPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page')),
                ('page_content', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('lookbookimage', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)))), icon='image', template='home/blocks/image_holder.html'))))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('home', '0005_auto_20150924_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookbookIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', auto_created=True, serialize=False, parent_link=True)),
                ('heading', models.CharField(max_length=100, blank=True)),
                ('intro', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='lookbookpage',
            name='cover_image',
            field=models.ForeignKey(blank=True, related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True, help_text='Lookbook cover images that displays in the Lookbook index page'),
        ),
        migrations.AddField(
            model_name='lookbookpage',
            name='heading',
            field=models.CharField(max_length=100, blank=True, help_text='ex) 2015 Winter Collection'),
        ),
        migrations.AddField(
            model_name='lookbookpage',
            name='intro',
            field=models.CharField(max_length=255, blank=True, help_text='Short intro(255 characters long) about this lookbook'),
        ),
        migrations.AlterField(
            model_name='lookbookpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('photo', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('style_number', wagtail.wagtailcore.blocks.CharBlock(required=False)))), icon='image', template='home/blocks/image_holder.html')),), blank=True, null=True),
        ),
    ]

from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from saleor.product.models import Product

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel,MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList


class HomePage(Page):

    def serve(self, request, *args, **kwargs):
        return render(request, self.template, {
            'self': self,
        })


class ShopPage(Page):

    def serve(self, request, *args, **kwargs):
        products = Product.objects.get_available_products()[:12]
        products = products.prefetch_related('categories', 'images',
                                         'variants__stock')
        return render(
            request, self.template,
            {
                'self': self,
                'products': products,
                'parent': None
            })


class LookbookImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    style_number = blocks.CharBlock(required=False)

    class Meta:
        icon = 'image'


class LookbookPage(Page):
    heading = models.CharField(max_length=100, blank=True, help_text="ex) 2015 Winter Collection")
    intro = models.CharField(max_length=255, blank=True, help_text="Short intro(255 characters long) about this lookbook")
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Lookbook cover images that displays in the Lookbook index page"
    )
    body = StreamField([
        ('photo', blocks.ListBlock(LookbookImageBlock(), template='home/blocks/image_holder.html', icon="image"))
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('heading', classname='full title'),
        FieldPanel('intro', classname='full'),
        ImageChooserPanel('cover_image'),
    ]
    streamfield_content_panels = [
        StreamFieldPanel('body'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(streamfield_content_panels, heading='lookbook'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])


class LookbookIndexPage(Page):
    heading = models.CharField(max_length=100, blank=True)
    intro = models.CharField(max_length=255, blank=True)

    subpage_types = ['home.LookbookPage']

    @property
    def lookbooks(self):
        lookbooks = LookbookPage.objects.live().descendant_of(self)

        return lookbooks

    def get_context(self, request, *args, **kwargs):
        lookbooks = self.lookbooks

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(lookbooks, 8)
        try:
            lookbooks = paginator.page(page)
        except PageNotAnInteger:
            lookbooks = paginator.page(1)
        except EmptyPage:
            lookbooks = paginator.page(paginator.num_pages)

        # Update template context
        context = super(LookbookIndexPage, self).get_context(request)
        context['lookbooks'] = lookbooks
        return context

    content_panels = Page.content_panels + [
        FieldPanel('heading', classname='full title'),
        FieldPanel('intro', classname='full'),
    ]

















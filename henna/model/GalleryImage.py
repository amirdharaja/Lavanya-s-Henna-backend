from django.db.models import Model, Manager, ImageField, DateTimeField, CharField


class GalleryImage(Model):

    PACKAGE = [
        ('cb', u'Classic Bridal'),
        ('eb', u'Elegant Bridal'),
        ('rb', u'Royal Bridal'),
        ('sb1', u'Star Bridal 1'),
        ('sb2', u'Star Bridal 2')
    ]

    HENNA_AREA = [
        ('h', u'Hands'),
        ('f', u'Foots'),
        ('o', u'Others')
    ]


    image            =    ImageField(upload_to='images/gallery_images', null=False)
    package           =    CharField(choices=PACKAGE, max_length=2, default='cb', null=True)
    henna_area           =    CharField(choices=HENNA_AREA, max_length=1, default='o', null=True)
    created_at      =    DateTimeField(auto_now_add=True, null=True)
    updated_at     =    DateTimeField(auto_now=True, null=True)

    objects = Manager()

    class Meta:
        db_table = "gallery_images"
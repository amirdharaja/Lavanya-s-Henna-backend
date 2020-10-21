from django.db.models import Model, Manager, FileField, BooleanField, DateTimeField


class PageImage(Model):

    image            =    FileField(upload_to='images/page_images', null=False)
    created_at      =    DateTimeField(auto_now_add=True, null=True)
    updated_at     =    DateTimeField(auto_now=True, null=True)

    objects = Manager()

    class Meta:
        db_table = "page_images"
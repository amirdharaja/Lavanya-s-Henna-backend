from django.db.models import Model, Manager, FileField, DateTimeField


class GalleryImage(Model):

    image            =    FileField(upload_to='images/gallery_images', null=False)
    created_at      =    DateTimeField(auto_now_add=True, null=True)
    updated_at     =    DateTimeField(auto_now=True, null=True)

    objects = Manager()

    class Meta:
        db_table = "gallery_images"
from django.db.models import Model, Manager, FileField, BooleanField, DateTimeField


class MainSlideImage(Model):

    image            =    FileField(upload_to='main_slide_images', null=False)
    created_at      =    DateTimeField(auto_now_add=True, null=True)
    updated_at     =    DateTimeField(auto_now=True, null=True)

    objects = Manager()

    class Meta:
        db_table = "main_slide_images"
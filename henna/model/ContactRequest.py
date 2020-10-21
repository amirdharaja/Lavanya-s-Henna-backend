from django.db.models import Model, Manager, CharField, TextField, BooleanField, DateTimeField


class ContactRequest(Model):

    name        =   CharField(max_length=255, blank=True)
    email       =   CharField(max_length=100, blank=True)
    phone       =   CharField(max_length=13, blank=True)
    details     =   TextField(blank=True)
    is_responsed     =   BooleanField(default=False)
    created_at  =   DateTimeField(auto_now_add=True, null=True)
    updated_at     =    DateTimeField(auto_now=True, null=True)


    objects = Manager()

    def __str__(self):
        return 'Contact Request By {}'.format(self.name)

    class Meta:
        db_table = "contact_requests"
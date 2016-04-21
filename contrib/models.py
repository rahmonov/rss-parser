from django.db import models


class CustomBaseModel(models.Model):
    """
    An abstract base class model that provides self-updating
    "created" and "modified" fields.
    """

    # Setting auto_now or auto_now_add to True will cause the field
    # to have editable=False and blank=True set.
    created = models.DateTimeField(auto_now_add=True, blank=False)
    modified = models.DateTimeField(auto_now=True, blank=False)

    # set to True if a particular record has been selected for removal.
    is_hidden = models.BooleanField(default=False, db_index=True)

    objects = models.Manager()  # the default manager

    # to extend Meta in child classes
    # use 'class Meta(CustomBaseModel.Meta):'
    class Meta:
        abstract = True

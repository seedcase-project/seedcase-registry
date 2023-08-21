from django.db import models
from django.db.utils import IntegrityError
from django.contrib.auth.models import User


class BaseManager(models.Manager):
    """
    The purpose to overriding normal Manager behaviour is to support
    case-insensitive matching.
    """

    def get(self, *args, **kwargs):
        return super(BaseManager, self).get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return super(BaseManager, self).filter(*args, **kwargs)


class BaseModel(models.Model):
    """
    Defines an abstract model built off of Django's Model class that
    provides some common fields that are useful across the application.
    """

    objects = BaseManager()

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    last_modified_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_related",  # avoid some reverse lookup clashes
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):
        # Check the unique_together constraints with any case
        # need to do manually to enforce the ability to have any case
        try:
            for unique_set in type(self)._meta.unique_together:
                get_args = {}
                for attr in unique_set:
                    get_args[attr] = getattr(self, attr, None)
                self._check_db_for_duplicate(get_args)
        except TypeError:
            pass

        return super(BaseModel, self).save(*args, **kwargs)

    def _check_db_for_duplicate(self, kwargs):
        if len(kwargs) == 0:
            return
        try:
            result = type(self).objects.filter(**kwargs).exclude(id=self.id)
            if len(result) > 0:
                raise IntegrityError("Entry already exists %s" % str(kwargs))
        except self.DoesNotExist:
            pass

    class Meta:
        abstract = True

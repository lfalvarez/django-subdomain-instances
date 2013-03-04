from django.db import models
from django.conf import settings

from .fields import DNSLabelField

class InstanceManager(models.Manager):
    def for_instance(self, instance):
        return self.get_query_set().filter(instance=instance)

class Instance(models.Model):
    label = DNSLabelField( db_index=True, unique=True )

    def __unicode__(self):
        return u'Instance %s' % self.label

    def get_absolute_url(self):
        url = 'http://%s.%s' % (self.label, getattr(settings, 'BASE_HOST', '127.0.0.1.xip.io'))
        if getattr(settings, 'BASE_PORT', None):
            url += ':' + settings.BASE_PORT
        return url

class InstanceMixin(models.Model):
    instance = models.ForeignKey(Instance)

    objects = InstanceManager()

    class Meta:
        abstract = True


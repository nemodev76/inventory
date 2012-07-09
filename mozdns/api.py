from tastypie.resources import ModelResource
from mozdns.domain.models import Domain
from tastypie.authorization import Authorization

from tastypie.api import Api

import pdb

class DomainResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        ret = super(DomainResource, self).obj_create(bundle, **kwargs)
        return ret

    class Meta:
        queryset = Domain.objects.all()
        authorization= Authorization()
        allowed_methods = ['get', 'post']

v1_dns_api = Api(api_name="v1_dns")
v1_dns_api.register(DomainResource())
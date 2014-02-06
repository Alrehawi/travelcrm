# -*-coding: utf-8-*-

import logging
import colander

from pyramid.view import view_config

from ..models import DBSession
from ..models.resource_type import ResourceType
from ..lib.qb.resources_types import ResourcesTypesQueryBuilder

from ..forms.resources_types import ResourceTypeSchema


log = logging.getLogger(__name__)


class ResourcesTypes(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(
        context='..resources.resources_types.ResourcesTypes',
        request_method='GET',
        renderer='travelcrm:templates/resources_types/index.mak',
        permission='view'
    )
    def index(self):
        return {}

    @view_config(
        name='list',
        context='..resources.resources_types.ResourcesTypes',
        permission='view',
        xhr='True',
        request_method='POST',
        renderer='json'
    )
    def list(self):
        qb = ResourcesTypesQueryBuilder(self.context)
        qb.sort_query(
            self.request.params.get('sort'),
            self.request.params.get('order', 'asc')
        )
        qb.page_query(
            int(self.request.params.get('rows')),
            int(self.request.params.get('page'))
        )
        return {
            'total': qb.get_count(),
            'rows': qb.get_serialized()
        }

    @view_config(
        name='add',
        context='..resources.resources_types.ResourcesTypes',
        request_method='GET',
        renderer='travelcrm:templates/resources_types/form.mak',
        permission='add'
    )
    def add(self):
        _ = self.request.translate
        return {
            'title': _(u"Add Resources Type")
        }

    @view_config(
        name="add",
        context="..resources.resources_types.ResourcesTypes",
        request_method="POST",
        renderer='json',
        permission="add"
    )
    def _add(self):
        schema = ResourceTypeSchema().bind(request=self.request)
        _ = self.request.translate
        try:
            controls = schema.deserialize(self.request.params)
            resource_type = ResourceType(
                humanize=controls.get('humanize'),
                name=controls.get('name'),
                resource=controls.get('resource'),
                description=controls.get('description'),
                resource_obj=self.context.create_resource(
                    controls.get('status')
                )
            )
            DBSession.add(resource_type)
            return {'success_message': _(u'Saved')}
        except colander.Invalid, e:
            return {
                'error_message': _(u'Please, check errors'),
                'errors': e.asdict()
            }

    @view_config(
        name='edit',
        context='..resources.resources_types.ResourcesTypes',
        request_method='GET',
        renderer='travelcrm:templates/resources_types/form.mak',
        permission='edit'
    )
    def edit(self):
        _ = self.request.translate
        resources_type = ResourceType.get(self.request.params.get('id'))
        return {
            'item': resources_type,
            'title': _(u"Edit Resources Type")
        }

    @view_config(
        name="edit",
        context="..resources.resources_types.ResourcesTypes",
        request_method="POST",
        renderer='json',
        permission="edit"
    )
    def _edit(self):
        _ = self.request.translate
        schema = ResourceTypeSchema().bind(request=self.request)
        resources_type = ResourceType.get(self.request.params.get('id'))
        try:
            controls = schema.deserialize(self.request.params)
            resources_type.humanize = controls.get('humanize')
            resources_type.name = controls.get('name')
            resources_type.resource = controls.get('resource')
            resources_type.description = controls.get('description')
            resources_type.resource_obj.status = controls.get('status')
            return {'success_message': _(u'Saved')}
        except colander.Invalid, e:
            return {
                'error_message': _(u'Please, check errors'),
                'errors': e.asdict()
            }

    @view_config(
        name='copy',
        context='..resources.resources_types.ResourcesTypes',
        request_method='GET',
        renderer='travelcrm:templates/resources_types/form.mak',
        permission='add'
    )
    def copy(self):
        _ = self.request.translate
        resources_type = ResourceType.get(self.request.params.get('id'))
        return {
            'item': resources_type,
            'title': _(u"Copy Resources Type")
        }

    @view_config(
        name='copy',
        context='..resources.resources_types.ResourcesTypes',
        request_method='POST',
        renderer='json',
        permission='add'
    )
    def _copy(self):
        return self._add()

    @view_config(
        name='delete',
        context='..resources.resources_types.ResourcesTypes',
        request_method='GET',
        renderer='travelcrm:templates/resources_types/delete.mak',
        permission='delete'
    )
    def delete(self):
        return {
            'id': self.request.params.get('id')
        }

    @view_config(
        name="delete",
        context="..resources.resources_types.ResourcesTypes",
        request_method="POST",
        renderer='json',
        permission="delete"
    )
    def _delete(self):
        _ = self.request.translate
        for id in self.request.params.getall('id'):
            resources_type = ResourceType.get(id)
            if resources_type:
                DBSession.delete(resources_type)
        return {'success_message': _(u'Deleted')}

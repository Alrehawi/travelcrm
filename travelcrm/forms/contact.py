# -*-coding: utf-8 -*-

import colander

from . import PhoneNumber, ResourceSchema


@colander.deferred
def contact_validator(node, kw):
    request = kw.get('request')

    validators = [colander.Length(min=2, max=64), ]
    if request.params.get('contact_type') == 'phone':
        validators.append(PhoneNumber())
    elif request.params.get('contact_type') == 'email':
        validators.append(colander.Email())

    return colander.All(*validators)


class ContactSchema(ResourceSchema):
    contact_type = colander.SchemaNode(
        colander.String(),
    )
    contact = colander.SchemaNode(
        colander.String(),
        validator=contact_validator
    )
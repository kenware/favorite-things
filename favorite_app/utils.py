# core Django import
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import serializers
# local import
from favorite_app.models import FavoriteThings
from favorite_app.constants import constant_messages


def re_order_ranking(validated_data, request):
    """
    re_order ranking such that ranking does not repeat when a new favorite
    things is added within a category

    Parameters:
        validated_data: validated data from the request
        request: request object
    """

    ranking = validated_data.get('ranking')
    category_id = request.data.get('category_id')
    favorite_things = FavoriteThings.objects.filter(
        ranking__gte=ranking, category_id=category_id)

    for favorite_thing in favorite_things:
        favorite_thing.ranking += 1

        favorite_thing.save()


def metadata_log(initial_data, new_metatada):
    """
    Generate audit log when during update on favorite things on metadata

    Parameters:
        initial_data: existing favoriteThings metadata to be updated
        new_metatada: Incoming(new) FavoriteThings metadata
    Returns:
        logs for metadata
    """
    messages = []
    for key, value in initial_data.items():
        new_value = new_metatada.get(key)
        if new_value:
            if new_value != value:
                messages.append(
                    constant_messages['meta_property_not_equall'].format(
                        key, value, new_value))
        else:
            messages.append(
                constant_messages['meta_property_removed'].format(key))
    for key, value in new_metatada.items():
        if key not in initial_data:
            messages.append(
                constant_messages['meta_property_addedd'].format(key))
    return messages


def gnerate_audit_log(instance, data):
    """
    Generate audit log when during update on favorite things

    Parameters:
        instance: existing favoriteThings data to be updated
        data: Incoming(new) FavoriteThings data
    Returns:
        audit log
    """

    initial_data = {
        'title': instance.title,
        'description': instance.description,
        'ranking': instance.ranking
    }
    audit_log = instance.audit_log
    message = []

    for key, value in initial_data.items():
        new_value = data.get(key)
        if new_value and new_value != value:
            message.append(constant_messages[key].format(value, new_value))
    message = message + metadata_log(instance.metadata, data.get('metadata'))
    if len(message):
        log = {
            'message': message,
            'date': f'{timezone.now()}'
        }
        audit_log.append(log)
    return audit_log


def validate_id(id):
    """
    validate an id

    Parameters:
        id: int
    Returns:
        Bool: True
        Response: Bad response
    """
    try:
        int(id)
    except ValueError:
        raise serializers.ValidationError({'status': constant_messages['invalid_id']})
    return True               
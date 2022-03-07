from .constants import *


def get_response_structure(**kwargs):
    structure = {}
    if kwargs['type'] == MESSAGE_NEW:
        structure['type'] = MESSAGE_NEW
        structure['data'] = kwargs['data']
        structure['dialog_name'] = kwargs['dialog_name']

    if kwargs['type'] == START_MESSAGE:
        structure['type'] = START_MESSAGE
        structure['data'] = 'This is start message'

    if kwargs['type'] == LOGIN_CODE:
        structure['type'] = LOGIN_CODE
        structure['code'] = kwargs['code']

    if kwargs['type'] == REGISTRATION_CODE:
        structure['type'] = REGISTRATION_CODE
        structure['code'] = kwargs['code']

    if kwargs['type'] == RECOVERY_CODE:
        structure['type'] = RECOVERY_CODE
        structure['code'] = kwargs['code']

    if kwargs['type'] == RECEIVE_REGISTRATION_CODE:
        structure['type'] = RECEIVE_REGISTRATION_CODE

    return structure

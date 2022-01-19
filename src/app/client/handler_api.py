
class Events:
    MESSAGE_NEW = 'message_new'
    LOGIN_CODE = 'login_code'
    REGISTRATION_CODE = 'registration_code'
    RECOVERY_CODE = 'recovery_code'

    RECEIVE_LOGIN_CODE = 'receive_login_code'
    RECEIVE_REGISTRATION_CODE = 'registration_code'
    RECEIVE_RECOVERY_CODE = 'receive_recovery_code'


def get_structure(**kwargs):
    structure = {}
    if kwargs['type'] == Events.MESSAGE_NEW:
        structure['type'] = Events.MESSAGE_NEW
        structure['data'] = kwargs['data']

    if kwargs['type'] == Events.LOGIN_CODE:
        structure['type'] = Events.LOGIN_CODE
        structure['code'] = kwargs['code']

    if kwargs['type'] == Events.REGISTRATION_CODE:
        structure['type'] = Events.REGISTRATION_CODE
        structure['code'] = kwargs['code']

    if kwargs['type'] == Events.RECOVERY_CODE:
        structure['type'] = Events.RECOVERY_CODE
        structure['code'] = kwargs['code']

    if kwargs['type'] == Events.RECEIVE_REGISTRATION_CODE:
        structure['type'] = Events.RECEIVE_REGISTRATION_CODE

    return structure
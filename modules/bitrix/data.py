from modules.bitrix.func_action import set_switch_states_work as bitrix_action


dir_auth = 'auth'


bitrix_data = {
    'bitrix': {
        'name': 'bitrix',
        'login': 'a.kuskov@make.st',
        'password': '-89hjkpZ!;',
        'link': 'b24.make.st/company/personal/user/79/tasks/',
        'action': bitrix_action,
        'file_cookies': dir_auth + '/bitrix_auth_cookies',
        'selectors': [
            'input[name="USER_LOGIN"]',
            'input[name="USER_PASSWORD"]',
            'input[type="submit"]'
        ]
    }
}

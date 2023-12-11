from modules.passwork.func_action import passwork_action


dir_auth = 'auth'


passwork_data = {
    'passwork': {
        'name': 'passwork',
        'login': 'a.kuskov@make.st',
        'password': 'qr0E6lUyvu',
        'link': 'passwork.make.st/enter#/login',
        'action': passwork_action,
        'file_cookies': None,
        'selectors': [
            '[pw-value="login"] input',
            '[pw-value="password"] input',
            '[ng-click="login()"]'
        ],
    },
}

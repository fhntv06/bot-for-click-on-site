from modules.gitlab.func_action import gitlab_action
from modules.gitlab.func_form import gitlab_form


dir_auth = 'auth'


# auth from google
gitlab_data = {
    'gitlab': {
        'name': 'gitlab',
        'login': '',
        'password': '',
        'link': 'https://gitlab.com/users/sign_in',
        'func_form': gitlab_form,
        'action': gitlab_action,
        'file_cookies': dir_auth + '/gitlab_auth_cookies'
    }
}

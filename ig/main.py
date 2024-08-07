'''
Module Main
'''

import json

from traceback import format_exc
from instagram.instagram import Instagram


def main() -> None:
    '''
    Function main
    '''
    ig_session = Instagram(
        user='',
        password='')

    ig_session.get_paths()
    ig_session.get_instagram()
    ig_session.extract()
    print(json.dumps(obj=ig_session.list_of_users))


if __name__ == '__main__':
    try:
        main()

    except Exception:
        ERROR = format_exc().replace('\n', ' ')
        print(ERROR)

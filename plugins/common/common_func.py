def get_sftp():
    print('sftp 작업을 시작합니다.')


def regist(name , sex , *args):
    print(f'이름 : {name}')
    print(f'성별: {sex}')
    print(f'그외 : {args}')

def regist2(name , sex , *args, **kwargs):
    print(f'이름 : {name}')
    print(f'성별: {sex}')
    print(f'그외 : {args}')
    email = kwargs.get('email') or None
    phone = kwargs.get('phone') or None
    if email : 
        print(email)
    if phone :
        print(phone)

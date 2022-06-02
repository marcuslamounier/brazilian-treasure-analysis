from os.path import exists

if exists('outputs/selic'):
    print('exists')
else:
    print('does not exist')
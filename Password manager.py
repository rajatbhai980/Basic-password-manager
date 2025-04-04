#basic password manager from scratch, learning source: techwithtim, Disclaimer not safe for use! XD

def add():
    Account = input('Enter your User ID: ')
    password = input('Enter your password: ')
    with open('password.txt', 'a') as f:
        f.write(Account +'|'+ password + '\n')
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print('User_Id : ', user, 'Password : ', passw)

def format():
    file = open('password.txt', 'w')
    file.write('')
    file.close()

while True:
    mode = input('Enter the mode(view, add, format), or press q to quit! ')

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    elif mode == 'format':
        format()
    elif mode == 'q':
        break
    else:
        print('Invalid mode! please try again!')

from random import randint

x = randint(1, 10)
user_num = 0
attempt = 0

while True:
    print('Men son oylab toptim ')
    user_num = int(input('Sonni topib koring:'))
    attempt += 1
    if user_num == x:
        print('Malades toptin.Senga suncha utunish ketti:'  + str(attempt))
        break
    elif user_num < x:
        print('Mening sonim kattaroq')
    elif user_num > x:
        print('Mening sonim kichikroq')
        



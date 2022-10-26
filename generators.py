import random


class Generators():

    #! написать метод с 3 параметрами (тип, кол-во символов)
    #! - text, numbers, mixed

    # Password generator
    def password_generator(self):
        psw = ''
        for x in range(12):
            psw = psw + \
                random.choice(
                    list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        return psw

    def number_generator(self):
        psw = ''
        for x in range(11):
            psw = psw + \
                random.choice(
                    list('123456789'))
        return psw

    def security_code_generator(self):
        psw = ''
        for x in range(7):
            psw = psw + \
                random.choice(
                    list('123456789'))
        return psw


    def pswd_generator(self):
        psw = ''
        for x in range(7):
            psw = psw + \
                random.choice(
                    list('123456789'))
        return psw


    def name_generator(self):
        psw = ''
        for x in range(7):
            psw = psw + \
                random.choice(
                    list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        return psw
    
    def zip_generator(self):
        zipn = ''
        for x in range(6):
            zipn = zipn + \
                random.choice(
                    list('123456789'))
        return zipn

    def email_generator(self, name):
        email_gen = name
        for x in range(5):
            email_gen = email_gen + random.choice(list('qwertyuiopasdfghjklzxcvbnm1234567890'))
        return email_gen + "@yandex.ru"
    
    def online_meeting_id_generators(self, name='test'):
        om_id = name + '-'
        for x in range(6):
            om_id = om_id + random.choice(list('qwertyuiopasdfghjklzxcvbnm1234567890-'))
        return om_id

    def access_code_generator(self):
        a_c = ''
        for x in range(9):
            a_c = a_c + random.choice(list('1234567890'))
        return a_c


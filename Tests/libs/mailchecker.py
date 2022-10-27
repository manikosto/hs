import imaplib
import os
import email
import time
import re
from data.data import Data
from config import Config


class Mailchecker:

    def __init__(self, login=Data.FCC_EMAIL_LOGIN, password=Data.FCC_EMAIL_PASSWORD, email_service=Data.EMAIL_SERVICE):
        self.login = login
        self.password = password
        self.email_service = email_service
        self.login_in()
        # self.get_last_message()

    def login_in(self):
        '''
        This method give access to email
        :param login: login from email
        :param password: password from email
        :return: access to account
        '''
        self.box = ""
        if os.environ['STAGE'].startswith('combase1'):
            self.box = "combase1"

        elif os.environ['STAGE'].startswith('combase2'):
            self.box = "combase2"

        elif os.environ['STAGE'].startswith('ui-standalone'):
            self.box = "ui-standalone"

        elif os.environ['STAGE'].startswith('integration'):
            self.box = "integration"

        elif os.environ['STAGE'].startswith('api'):
            self.box = "api"

        elif os.environ['STAGE'].startswith('mobile'):
            self.box = "mobile"

        self.mail = imaplib.IMAP4_SSL(self.email_service)
        self.mail.login(self.login, self.password)
        self.mail.list()
        self.mail.select(self.box)

    def get_last_message(self):
        result, data = self.mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data = self.mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        self.raw_email_string = raw_email.decode('utf-8', errors='ignore')

    def get_body_message(self):
        '''
        This method return message body
        :return: body
        '''
        body = ""
        self.email_message = email.message_from_string(self.raw_email_string)
        if self.email_message.is_multipart():
            for part in self.email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(
                        decode=True)  # to control automatic email-style MIME decoding (e.g., Base64, uuencode, quoted-printable)
                    body = body.decode()
                elif part.get_content_type() == "text/html":
                    continue

    def get_letter_subject(self, message_subject):
        '''
        This method return message subject
        :param subject: message subject
        :return: letter subject
        '''
        self.get_last_message()
        self.get_body_message()  # get last message
        time_count = 0
        count = 0
        subj = ""
        if "qa" in os.environ['STAGE']:
            subject = "QA MODE:" + message_subject
        else:
            subject = message_subject
        while subj != subject:
            self.login_in()
            self.get_last_message()
            self.get_body_message()
            subj = self.email_message["Subject"]
            print(subj)
            if subj == subject:
                return str(subject)
            if time_count >= 30:
                assert subj == subject, "Message was not received"
            else:
                time.sleep(2)
                time_count += 1
                count += 1

    def verify_email_checking(self, message_subject):
        self.get_last_message()  # get last message
        self.get_body_message()  # get last message
        time_count = 0
        count = 0
        subj = ""
        subject = ""
        link = str(Config.config[os.environ['STAGE']]['DOMAIN'])

        if "qa" in os.environ['STAGE']:
            subject = "QA MODE:" + message_subject
        else:
            subject = message_subject

        while subj != subject:
            self.login_in()
            self.get_last_message()
            self.get_body_message()
            subj = self.email_message["Subject"]
            print(subj)
            if subj == subject:
                lst = re.findall(
                    r""+link+"/verify-email/\d+\W+\d+\W+[a-z0-9]+", self.raw_email_string)
                print(lst[0])
                return lst[0]
            if time_count >= 30:
                assert subj == subject, "Verified message is not received"
            else:
                time.sleep(2)
                time_count += 1

    # def reset_password_link_checking(self):
    #     self.get_last_message()
    #
    #     if os.environ['STAGE'].startswith('stf'):
    #         self.box = "STF"
    #
    #     elif os.environ['STAGE'].startswith('fcc'):
    #         if "qa" in os.environ['STAGE']:
    #             lst = re.findall(r'qa-www.freeconferencecall.com/reset-password/\d+\W+\d+\W+[a-z0-9]+',self.raw_email_string)
    #             return lst[0]
    #         else:
    #             lst = re.findall(r'www.freeconferencecall.com/reset-password/\d+\W+\d+\W+[a-z0-9]+',self.raw_email_string)
    #             return lst[0]
    #
    #     elif os.environ['STAGE'].startswith('sm'):
    #         if "qa" in os.environ['STAGE']:
    #             lst = re.findall(r'qa-www.startmeeting.com/reset-password/\d+\W+\d+\W+[a-z0-9]+', self.raw_email_string)
    #             return lst[0]
    #         else:
    #             lst = re.findall(r'www.startmeeting.com/reset-password/\d+\W+\d+\W+[a-z0-9]+', self.raw_email_string)
    #             return lst[0]
    #
    #     elif os.environ['STAGE'].startswith('hd'):
    #         self.box = "FCC-HD"
    #
    #     elif os.environ['STAGE'].startswith('team'):
    #         self.box = "TEAM"

    def get_headers(self, header):
        '''
        This method return message header
        :param header:
        - To
        - From
        - Subject
        - Date
        :return: Header
        '''
        self.get_last_message()
        self.get_body_message()
        print(self.email_message[header])


    def invitation_team(self, message_subject):
        self.get_last_message()  # get last message
        self.get_body_message()  # get last message
        time_count = 0
        count = 0
        subj = ""
        subject = ""
        link = str(Config.config[os.environ['STAGE']]['DOMAIN'])

        if "qa" in os.environ['STAGE']:
            subject = "QA MODE:" + message_subject
        else:
            subject = message_subject

        while subj != subject:
            self.login_in()
            self.get_last_message()
            self.get_body_message()
            subj = self.email_message["Subject"]
            print(subj)
            if subj == subject:
                lst = re.findall(
                    r""+link+"/invite/\d+\W+\d+\W+[a-z0-9]+", self.raw_email_string)
                print(lst[0])
                return lst[0]
            if time_count >= 30:
                assert subj == subject, "Verified message is not received"
            else:
                time.sleep(2)
                time_count += 1

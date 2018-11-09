from http.server import BaseHTTPRequestHandler, HTTPServer
import smtplib
import imaplib
import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PORT = 8081
HOST = 'localhost'

is_test = True


class SMTPserver:
    def __init__(self, server_email, server_name, server_port,
                 imap=None, imap_port=None,
                 username=None, password=None):

        self.server_email = server_email
        self.server_name = server_name
        self.server_port = server_port

        self.username = username
        self.password = password

        self.imap = imap
        self.imap_port = imap_port

        self.server = smtplib.SMTP_SSL(server_name, server_port)
        self.imap_server = imaplib.IMAP4_SSL(imap)

        if is_test:
            self.server.set_debuglevel(True)

        self.server.ehlo()
        self.server.login(username, password)
        self.imap_server.login(username, password)

    def send_message(self, msg_text, from_who, from_who_addr,
                           to_who, to_email, subject):

        msg = MIMEText(msg_text)
        msg.set_unixfrom(from_who)
        msg['To'] = email.utils.formataddr((to_who, to_email))
        msg['From'] = email.utils.formataddr((from_who, from_who_addr))
        msg['Subject'] = subject

        self.server.sendmail(self.server_email, [to_email], msg.as_string())


if is_test:
    test_server_email = 'ksistest@yandex.ru'

    # SMTP
    test_server_name = 'smtp.yandex.ru'
    test_server_port = 465

    # IMAP
    test_imap = 'imap.yandex.ru'
    test_imap_port = 993

    test_username = "KsisTest"
    test_password = 'ksistest1'

    test_msg = 'Test message'
    test_from_who = 'Ksis'
    test_from_whoaddr_email = 'ksistest@yandex.ru'
    test_to = 'ALEX'
    # test_to_email = 'alexmay997@gmail.com'
    test_to_email = 'zhenyagamonyuk@gmail.com'
    test_subject = 'Test'

    server = SMTPserver(test_server_email, test_server_name, test_server_port,
                        test_imap, test_imap_port,
                        test_username, test_password)

    server.send_message(test_msg, test_from_who, test_from_whoaddr_email,
                        test_to, test_to_email, test_subject)
    # imap = server.imap_server
    # boxes = imap.list()
    # box = imap.select()
    # mail = imap.search(None, 'ALL')
    # status, data = imap.fetch(b'1', '(RFC822)')
    # msg = email.message_from_bytes(data[0][1], _class=email.message.EmailMessage)
    # subj = msg['Subject']





# class HttpProcessor(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('content-type', 'text/html')
#         self.end_headers()
#         self.wfile.write("<p>hello !</p>")
#
#
# serv = HTTPServer((HOST, PORT), HttpProcessor)
# serv.serve_forever()

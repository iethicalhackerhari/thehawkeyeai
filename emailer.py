import email
import smtplib, ssl
from threading import Thread

class Mail(Thread):

    def __init__(self, emails, subject, content):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "thehawkeyeai@gmail.com"
        self.password = "woxdayeajejewjhj"
        self.emails= emails
        self.subject= subject
        self.content= content
        Thread.__init__(self)

    
    def run(self):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        for email in self.emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {self.subject}\n{self.content}")
            print(result)

        service.quit()


if __name__ == '__main__':
    mails = input("Enter emails: ").split()
    subject = input("Enter subject: ")
    content = input("Enter content: ")

    mail = Mail()
    mail.send(mails, subject, content)

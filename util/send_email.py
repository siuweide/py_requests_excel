import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendEmail(count_case, success_count,fail_count):
    mail_host = "smtp.qq.com"
    mail_user = "2112296725@qq.com"
    mail_pass = 'xxxxx'

    sender = '2112296725@qq.com'
    receivers = ["328527390@qq.com"]

    text = '这次接口自动化回归测试，总共运行了%d条用例，成功的用例有%d条，失败的有%d条。' %(count_case, len(success_count), len(fail_count))
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header('siuweide<212296725@qq.com>', 'utf-8')
    message['to'] = Header('siuweide', 'utf-8')

    subject = 'Pyton SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException:
        print('无法发送邮件')
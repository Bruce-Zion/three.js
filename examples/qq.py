import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"
mail_user = "jero2008@qq.com"
mail_pass = "ylvezuksvokmdfij"

sender = 'jero2008@qq.com'
receivers = ['jero2008@aliyun.com']

message = MIMEText('EOS hash notification...', 'plain', 'utf-8')
message['From'] = Header("JeroQQ", 'utf-8')
message['To'] = Header("JeroAliyun", 'utf-8')
subject = 'EOS hash notification...'
message['Subject'] = Header(subject, 'utf-8')

try:
    print('1')
    smtpObj = smtplib.SMTP_SSL(mail_host, 587) #465 or 587
    print('2')
    smtpObj.set_debuglevel(1)
    print('3')
    smtpObj.login(mail_user, mail_pass)
    print('4')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('5')
    smtpObj.quit()
    print("Mail has been sent successfully.")    
except smtplib.SMTPException as e:
    print(e)
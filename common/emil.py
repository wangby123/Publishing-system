# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----------1.跟发件相关的参数------

smtpserver = "smtp.163.com"                         # 发件服务器
port = 465                                           # 端口
sender = "mengmengxidi@163.com"                    # 账号
psw = "qq163com1"                                   # 密码
receiver = "429172016@qq.com"                      # 接收人

# ----------2.编辑邮件的内容------

# 读文件
file_path = r"C:\test\report\result.html"
with open(file_path, "rb") as fp:
    mail_body = fp.read()

msg = MIMEMultipart()
msg["from"] = sender                               # 发件人
msg["to"] = receiver                               # 收件人
msg["subject"] = "秦能的自动化测试报告"                   # 主题

# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)

# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)

# ----------3.发送邮件------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()



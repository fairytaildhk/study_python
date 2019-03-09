# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 18:47
# @Author  : huangkaiding
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def sendMail():
    mail_host = 'mail.blackfish.cn'
    name = "btctest"
    password = "1qaz@WSX"

    sender = 'btctest@blackfish.cn'
    receivers = ['huangkaiding@blackfish.cn',
                 'skyeli@blackfish.cn',
                 'huaishengsong@blackfish.cn',
                 'lukazhou@blackfish.cn',
                 'qizhang@blackfish.cn',
                 'stonerchen@blackfish.cn',
                 'verasun@blackfish.cn',
                 'binchengzhang@blackfish.cn']
    # ['zaneyao@blackfish.cn']

    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = Header("凯哥给你发邮件了", 'utf-8')  # 发送者
    for receiver in receivers:
        msgRoot['To'] = Header(receiver, 'utf-8')  # 接收者
    subject = '酒店订单统计'
    msgRoot['Subject'] = Header(subject, 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    mail_msg = """
    <p><a href="https://github.com/fairytaildhk">给凯哥的github项目点个star</a></p>
    <p>订单统计图：</p>
    <p><img src="cid:image1"></p>
    """
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # 指定图片为当前目录
    fp = open('order.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    try:
        smtp = smtplib.SMTP(host=mail_host, port=587)
        # smtp.connect(host=mail_host, port=587)
        smtp.starttls()
        smtp.login(name, password)
        smtp.sendmail(sender, receivers, msgRoot.as_string())
        smtp.quit()
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    sendMail()

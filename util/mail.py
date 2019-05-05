# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 18:47
# @Author  : huangkaiding
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def sendMail(mail_host, name, password, sender):

    receivers = []
    # receivers = ['xxxx@qq.com',
    #              'xxxx@qq.com',]

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
    <h2 align="left">给凯哥的github项目点个star，关注一下凯哥的博客呀！！！</h2>
    <p>(提示：点击图片即可)</p>

    <p align="left">
        <p>凯哥的gitHub</p>
        <a href="https://github.com/fairytaildhk">
            <img border="0" src="cid:image3" width="120" height="60" align ="">
        </a>
        <p>凯哥的博客</p>
         <a href="https://blog.csdn.net/weixin_41576586">
            <img border="0" src="cid:image2" width="120" height="60">
         </a>
  </p>
  <!--<h2>凯哥的博客</h2>-->
  <!--<p align="left">-->
    <!--<a href="https://blog.csdn.net/weixin_41576586">-->
      <!--<img border="0" src="logo.png" width="120" height="60">-->
    <!--</a>-->
  <!--</p>-->
  <hr/>
  <h1 align="left" style="font-family:arial;color:#4e6eff;font-size:20px;">订单统计图：</h1>
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

    # 图片logo
    fp1 = open('logo.png', 'rb')
    msgImage1 = MIMEImage(fp1.read())
    fp1.close()
    msgImage1.add_header('Content-ID', '<image2>')
    msgRoot.attach(msgImage1)

    # 图片marvellogo
    fp2 = open('marvellog.jpg', 'rb')
    msgImage2 = MIMEImage(fp2.read())
    fp2.close()
    msgImage2.add_header('Content-ID', '<image3>')
    msgRoot.attach(msgImage2)

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




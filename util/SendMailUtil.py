# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 20:45
# @Author  : huangkaiding
from util import HttpRequestsUtil


def send_mail(recipientEmails, subject, msgText, ccEmails=None, files=None):
    """
    发邮件方法
    :param recipientEmails: String[] 必传 收件人列表
    :param subject: String 必传 邮件主题
    :param msgText: String 必传 邮件内容  （可以是HTML格式内容 可以使TEXT 格式内容）
    :param ccEmails: String[] 可选 抄送人列表
    :param files: List<FileModel> 可选 附件列表 (必须是内网可访问非加密的URL地址)，附件内容不能大于5M
    :return:
    """
    if files is None:
        files = []
    if ccEmails is None:
        ccEmails = []
    url = "http://api.mail.fbs.sit.blackfi.sh/mail/api/sendMail"
    params = {
        "systemCode": "htp",
        "recipientEmails": recipientEmails,
        "ccEmails": ccEmails,
        "files": files,
        "subject": subject,
        "msgText": msgText,
        "businessCode": "htp_20181212"
    }
    return HttpRequestsUtil.doPost(url, params)

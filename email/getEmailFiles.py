# -*- coding:utf-8 -*-
# author:HHQ
# datetime:2023/6/27 21:50
# software: PyCharm


import imaplib
import email
import os
from email.header import decode_header

# 邮箱服务器地址和端口
imap_server = 'imap.exmail.qq.com'
imap_port = 993

# 邮箱用户名和密码
email_user = 'nancy.nie@farben.com.cn'
email_password = ''

# 连接到IMAP服务器
mail = imaplib.IMAP4_SSL(imap_server, imap_port)
mail.login(email_user, email_password)

# print(mail.login(email_user, email_password))

# 选择收件箱
mail.select('inbox')

# 获取最新的邮件
_, data = mail.search(None, 'ALL')
mail_ids = data[0].split()
latest_mail_id = mail_ids[-1]
#
_, data = mail.fetch(latest_mail_id, '(RFC822)')
raw_email = data[0][1]
msg = email.message_from_bytes(raw_email)
subject = decode_header(msg["Subject"])[0][0].decode()
print(f'最新邮件主题: {subject}')
#
# # 下载最新邮件的附件
# for part in msg.walk():
#     if part.get_content_maintype() == 'multipart':
#         continue
#     if part.get('Content-Disposition') is None:
#         continue
#
#     file_name = part.get_filename()
#     file_path = os.path.join('attachments', file_name)
#     with open(file_path, 'wb') as f:
#         f.write(part.get_payload(decode=True))
#     print(f'下载附件: {file_name}')
#
# # 根据发件人获取最新的几封邮件
# sender_email = 'sender@example.com'
# num_emails = 3  # 获取的邮件数量
#
# _, data = mail.search(None, f'FROM "{sender_email}"')
# mail_ids = data[0].split()
# latest_sender_mail_ids = mail_ids[-num_emails:]
#
# for mail_id in latest_sender_mail_ids:
#     _, data = mail.fetch(mail_id, '(RFC822)')
#     raw_email = data[0][1]
#     msg = email.message_from_bytes(raw_email)
#     subject = decode_header(msg["Subject"])[0][0].decode()
#     print(f'来自 {sender_email} 的邮件主题: {subject}')
#
#     # 下载邮件附件
#     for part in msg.walk():
#         if part.get_content_maintype() == 'multipart':
#             continue
#         if part.get('Content-Disposition') is None:
#             continue
#
#         file_name = part.get_filename()
#         file_path = os.path.join('attachments', file_name)
#         with open(file_path, 'wb') as f:
#             f.write(part.get_payload(decode=True))
#         print(f'下载附件: {file_name}')

# 退出并关闭连接
mail.logout()
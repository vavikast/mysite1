# -*- coding: utf-8 -*-
2018 - 10 - 31
__author__ = 'Felix'
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    subject, from_email, to = '来自www.liujiangblog.com的测试邮件', 'kalai2113@sina.com', '486892195@qq.com'
    text_content = '欢迎访问www.vavikast.com，这里是王伟的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.vavikast.com" target=blank>www.vavikast.com</a>，这里是felix的博客和教程站点，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
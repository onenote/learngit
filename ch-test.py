#! /usr/local/bin/ python
# -*- coding: utf-8 -*-

print u'中文测试'
print '------------------------------'

print '-----------------START------------------'
name = raw_input(u'请输入一个中文名字：'.encode('gbk')).decode('gbk')
print '--------%s' % name
print 'The name is', name
print u'输入名称为: %s' % (name)
print '-----------------END------------------'
#comment1

# -*- coding: utf-8 -*-
##############################################################################
#
#    QQ field
#    Copyright 2013 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name' : 'OpenERP intlTelInput',
    'version': '1.0',
    'summary': 'intlTelInput',
    'sequence': '19',
    'category': 'Tools',
    'complexity': 'easy',      
    'description': """
自定义widget，用于输入国际电话号码。它增加了国旗下拉任何输入,列出所有国家及其国际拨号代码旁边他们的旗帜

""",
    'depends' : ['web'],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': [
        'images/int.jpg',
        
    ],
}

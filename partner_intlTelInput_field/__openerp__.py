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
    'name': 'intlTelInput_field',
    'version': '0.1',
    'category' : 'Sales Management',
    'description': """
用于输入国际电话号码。它增加了国旗下拉任何输入,列出所有国家及其国际拨号代码旁边他们的旗帜

""",
    'author': ' l21',
    'website': 'www.viewtop.cn/191433230@qq.com',
    'depends': ['base','web_intlTelInput_widget'],
    'data': [
           'res_partner_view.xml',
    ],
    'installable': True,
    'images': [
        'images/int.jpg',
        
    ],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

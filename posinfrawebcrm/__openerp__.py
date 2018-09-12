# -*- coding: utf-8 -*-
{
    'name': "POSinfraestructuraWEB.CRM",

    'summary': """
        Integración infraestructura particular de reglas de negocio , 
        para POS WEB y CRM compatible con la version 9.0 del ERP. 
        requiere de los módulos 'base y correos'
     """,

    'description': """
        This module modifies POS WEB integration and CRM to satisfy especifics rules of bussiness.
        Este modulo modifica la integración POS WEB y CRM deacuerdo a reglas de negocio particulares.
    """,

    'author': "SCL-FOTOCOPIADORAS/SOFTWEB365",
    'website': "http://www.softweb365.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [        
        #'security/access.infrasan.xml',
        #'security/ir.model.access.csv'
        'views/views.xml', 
        'views/templates.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

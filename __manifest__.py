# -*- coding: utf-8 -*-
{
    'name': "Estate",
    'summary': """Real estate management""",
    'description': """
        Real estate management module
    """,
    'license': 'LGPL-3',
    'author': "Imad Bourouche",
    'email': "ji_bourouche@esi.dz",
    'category': 'Administration',
    'version': '0.1',
    'application': True,
    #'depends': [],
    'data': [
        #'data/estate.property.type.csv',
        #'data/estate.property.csv',
        'security/ir.model.access.csv',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',

        'views/estate_menus.xml'
    ],
    #'demo': [
    #'demo.xml',
    #],
}
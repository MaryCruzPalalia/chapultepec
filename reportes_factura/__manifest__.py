# -*- coding: utf-8 -*-
{
    'name': "reportes_factura",
    'summary': """Agregar campos a factura
    """,
    'description': """
        Modulo para para agregar unos campos de facturas
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
        
        ],

	'data': [ 
   'views/reporte_factura.xml',
   'views/factura_vista.xml',
#    'data/categorias.xml',
    ],
	'demo':[
	],
    'installable':True,
}

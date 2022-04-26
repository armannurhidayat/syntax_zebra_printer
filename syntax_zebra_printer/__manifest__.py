# -*- coding: utf-8 -*-
# ©  2021 armannurhidayat
{
    'name': "Zebra Printer Integration",
    'summary': "Zebra Printer Integration",
    'price': "10",
	'license': "OPL-1",
	'currency': "USD",
    'description': """
        Zebra barcode printer integration for module stock: Lots/Serial Numbers
        Tested on a zebra printer type
        - ZD888
    """,
    'author': "Arman Nur Hidayat",
    'website': "http://www.armannurhidayat.com",
    "images": ["static/description/logo.png"],
    'category': 'Stock',
    'version': '12.0.1',
    'depends': ['base','stock','barcodes'],
    'installable': True,
    "development_status": "stable",
    'data': [
        'views/assets.xml',
        'views/stock_production_lot.xml',
        'views/res_config_settings_view.xml',
    ],
}

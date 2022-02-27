# -*- coding: utf-8 -*-
# ©  2021 armannurhidayat
{
    'name': "Zebra printers integration",
    'summary': "Zebra printers integration",
    'price': "10",
	'license': "OPL-1",
	'currency': "USD",
    'description': "Zebra barcode printers integration for module stock: Lots/Serial Numbers",
    'author': "Arman Nur Hidayat",
    'website': "http://www.armannurhidayat.com",
    "images": ["static/description/logo.jpg"],
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
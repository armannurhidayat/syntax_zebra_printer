# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import api, fields, models


class ResCompany(models.Model):
	_inherit = 'res.company'

	type = fields.Selection([
		('qr', 'QR Code'),
		('barcode', 'Barcode'),
	], string='Type', default='qr', translate=True)

# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	type = fields.Selection([
		('qr', 'QR Code'),
		('barcode', 'Barcode'),
	], string='Type', default='qr', related='company_id.type', translate=True, readonly=False)
	paper_size = fields.Selection([
		# ('55x25', '55mmx25mm'),
		('50x30', '50mmx30mm'),
		# ('50x20', '50mmx20mm'),
		], string='Paper Size', default='50x30')

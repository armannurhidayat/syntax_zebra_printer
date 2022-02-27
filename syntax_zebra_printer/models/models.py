# -*- coding: utf-8 -*-

from odoo import models, fields, api
from simple_zpl2 import ZPLDocument, QR_Barcode, Code128_Barcode
from PIL import Image
import io

class StockProductionLot(models.Model):
	_inherit = 'stock.production.lot'

	data_print = fields.Char(string="Data Print", readonly=False, compute='_generate_command')

	@api.multi
	def action_print(self):
		pass


	def _generate_command(self):
		for lot in self:
			zpl = ZPLDocument()

			if self.env.user.company_id.sudo().type == "qr":
				if len(lot.product_id.name) >= 16:
					zpl.add_field_origin(250, 100, '0')
					zpl.add_font('C', zpl._ORIENTATION_NORMAL, 20)
					zpl.add_field_data(lot.product_id.name[0:16])
					zpl.add_field_origin(250, 120, '0')
					zpl.add_font('C', zpl._ORIENTATION_NORMAL, 20)
					zpl.add_field_data(lot.product_id.name[16:])

				if len(lot.product_id.name) <= 16:
					zpl.add_field_origin(250, 100, '0')
					zpl.add_font('C', zpl._ORIENTATION_NORMAL, 20)
					zpl.add_field_data(lot.product_id.name)

				zpl.add_field_origin(300, 160, '0')
				zpl.add_font('C', zpl._ORIENTATION_NORMAL, 20)
				zpl.add_field_data('{} {}'.format(lot.product_qty, lot.product_uom_id.name))

				zpl.add_field_origin(450, 50)
				qr_data = 'QA,{}'.format(lot.name)
				qr = QR_Barcode(qr_data, 2, 6, zpl._QR_ERROR_CORRECTION_STANDARD)
				zpl.add_barcode(qr)

			elif self.env.user.company_id.sudo().type == "barcode":
				zpl.add_field_origin(420, 30)
				barcode_data = '{}'.format(lot.name)
				bc = Code128_Barcode(barcode_data, 'N', 10, 'Y')
				zpl.add_barcode(bc)
			
			lot.data_print = zpl.zpl_text

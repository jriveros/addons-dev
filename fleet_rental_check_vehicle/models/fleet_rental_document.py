# -*- coding: utf-8 -*-
import openerp
from openerp import models, fields, api

class FleetRentalDocument(models.Model):
    _inherit = 'fleet_rental.document'

    check_line_ids = fields.One2many('fleet_rental.check_line', 'document_id', string='Vehicle rental checklist')

    @api.model
    def default_get(self, fields_list):
        result = super(FleetRentalDocument, self).default_get(fields_list)
        document_id= self._context.get('active_id', False)
        items = self.env['fleet_rental.item_to_check'].search([])
        check_line_obj = self.env['fleet_rental.check_line']

        if len(items) > 0:
           result['check_line_ids'] =  [(0, 0, {'item_id': items[0].id})]
        return result


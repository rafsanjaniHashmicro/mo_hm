from odoo import models

class SaleInherit(models.Model):
    _inherit = 'sale.order'

    def create_mo(self):

        for record in self:
            for i in record.order_line:
                execute_bom = i.product_id.bom_ids.id
                if execute_bom:
                    i.env['mrp.production'].create(
                        {'product_id': i.product_id.id,
                         "product_uom_id": i.product_uom.id,
                         "bom_id": i.product_id.bom_ids.id,
                         "product_qty": i.product_uom_qty})
                else:
                    pass

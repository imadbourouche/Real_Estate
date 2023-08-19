from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Real estate Offers"
    price = fields.Float(string="Price")
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], string='Status', copy=False)
    partner = fields.Many2one('res.partner', string='Partner', required=True)
    estate_property = fields.Many2one('estate.property', string='Property', required=True)
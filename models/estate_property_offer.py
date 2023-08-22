from odoo import fields, models, api
from datetime import datetime, timedelta


class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Real estate Offers"
    price = fields.Float(string="Price")
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], string='Status', copy=False)
    partner = fields.Many2one('res.partner', string='Partner', required=True)
    estate_property = fields.Many2one('estate.property', string='Property', required=True, readonly=True)
    
    validity = fields.Integer(string='Validity', default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline", store=True)

    # Computed field
    @api.depends('validity')
    def _compute_date_deadline(self):
        for offer in self:
            offer.date_deadline = datetime.now() + timedelta(days=offer.validity)

    # Inverse function
    def _inverse_date_deadline(self):
        for offer in self:
            if offer.date_deadline:
                offer.validity = (offer.date_deadline - datetime.now().date()).days
            else:
                offer.validity = 20
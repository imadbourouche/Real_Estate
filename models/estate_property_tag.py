from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="Real estate tag"
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string='Description')

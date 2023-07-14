from odoo import fields, models

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description="The real estate type"
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string='Description')

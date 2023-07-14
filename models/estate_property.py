from odoo import fields, models
from datetime import date, timedelta

default_availability_date = (date.today() + timedelta(days=90)).strftime("%Y-%m-%d")

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property description"


    name = fields.Char(string="Name", required=True)
    estate_type = fields.Many2one("estate.property.type", string="Type")
    active = fields.Boolean(string="Active", default=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability',copy=False,default=default_availability_date)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price',readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms',default=2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), (
        'east', 'East'), ('west', 'West')], string='Garden Orientation')
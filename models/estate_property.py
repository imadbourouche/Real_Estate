from odoo import fields, models, api
from datetime import date, timedelta

default_availability_date = (date.today() + timedelta(days=90)).strftime("%Y-%m-%d")

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property description"

    # General types of fields
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string="Active", default=True)
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability',copy=False,default=default_availability_date)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price',readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms',default=2)
    living_area = fields.Float(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Float(string='Garden Area')
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string='Garden Orientation')


    # ------- Relationship -------- #
    # Many2many relationship
    tags = fields.Many2many("estate.property.tag", string="Tags")
    
    # Many2one relationship
    estate_type = fields.Many2one("estate.property.type", string="Type")
    sales_person = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', copy=False)

    # One2many relationship
    offers = fields.One2many("estate.property.offer","estate_property")



    # ------- Computed fields -------- #
    total_area = fields.Float(string='Total Area', compute='_compute_total_area', store=True)

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area


    best_price = fields.Float(string="Best Offer", compute="_compute_best_price", store=True)

    @api.depends("offers.price")
    def _compute_best_price(self):
        for property in self:
            best_price = max(property.offers.mapped("price"), default=0.0)
            property.best_price = best_price


    # onchange
    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden :
            self.garden_area = 10
            self.garden_orientation = 'north'
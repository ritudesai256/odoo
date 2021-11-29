
from odoo import models,fields


class EstateProperty(models.Model):
    _name = 'estate.property'

    _description = "Test Model"

    name = fields.Char()
    
  
    name = fields.Char( string="Property Name",default="Unknown",required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date("Last Seen", default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False,readonly=True)
    bedrooms = fields.Integer(default=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')        
        ])

    #active=fields.Boolean() 
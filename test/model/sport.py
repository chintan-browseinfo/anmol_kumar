from odoo import models, api, fields, _


class SportModule(models.Model):
    _name="sport.module"
    _description="Sport Info"
    
    name = fields.Char(string="Name")
    length=fields.Integer(string="length of equipment")
    weight=fields.Integer(string="weight of equipment")
    brandname=fields.Selection([('n','nike'), ('a','addidas'),('r','reebok'),('e','espn'),('s','Sky Sports')],required=True,note = fields.Text(string='Description'))
    account_id = fields.One2many('customer.info','buyer_id' 'buyer')
    account_info=fields.Many2many('customer.info','buyer_account_id','buyer_id','customer_id',string='important')



class Customer(models.Model):
	_name = "customer.info"
	_description = "Customer Info"

	name = fields.Char(string='Customer Reference', required=True, copy=False)
	first_name = fields.Char(string='First Name', required=True, copy=False)
	middle_name = fields.Char(string='Middle Name', required=True, copy=False)
	last_name = fields.Char(string='Family Name', required=True, copy=False)
	customer_id = fields.One2many('customer.info', 'customer.id', 'buyer')
	buyer_id=fields.Many2one('sport.module','x',select=True)
	buyer_ids=fields.Many2many('sport.module','customer_id','buyer_id',string='important details')

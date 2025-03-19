from odoo import models, fields, api

class ExampleModel(models.Model):
    _name = 'example.model'
    _description = 'Example Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)
    
    @api.model
    def create(self, vals):
        # Example of overriding create method
        return super(ExampleModel, self).create(vals)

    def write(self, vals):
        # Example of overriding write method
        return super(ExampleModel, self).write(vals)

    def unlink(self):
        # Example of overriding unlink method
        return super(ExampleModel, self).unlink()
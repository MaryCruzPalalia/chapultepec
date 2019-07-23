from odoo import models, fields, api
from odoo.exceptions import ValidationError

    
class dependsModel(models.Model):
    _inherit = 'account.invoice'


    @api.depends('name')
    def _compute_depends(self):
        print(self.partner_id)
        print(self.id)
        print(self.name)
        print(self.display_name)
        print(self.partner_id.name)
        print(self.partner_id.name)
        print(self.partner_id.name)
        print(self.partner_id.name)
        print(self.commercial_partner_id.name)
#        alumno=self.env['op.student'].search([('invoice_ids','=',self.id)])
        alumno=self.env['op.student'].search([('partner_id.id','=',self.partner_id.id)])
        print(alumno.name)
        print(alumno)
        print(alumno.x_matricula)
        self.x_estudiante=alumno #cacho los datos del estudiante del modelo op.student solo en reporte hay que modificar que dato queremos
        self.x_student=alumno.name
        print(self.x_estudiante.course_detail_ids.batch_id.name) #grupo de studiante 
        print(self.x_estudiante.course_detail_ids.course_id.name)


    # @api.constrains('x_student')
    # def _check_something(self):
    #     print(self.partner_id)
    #     print(self.id)
    #     print(self.name)
    #     print(self.display_name)
    #     alumno=self.env['op.student'].search([('invoice_ids','=',self.id)])
    #     if(alumno):
    #         self.x_student=alumno
    #         print(self.x_student) 
    #         print(self.x_student.name)


    x_estudiante=fields.Many2one('op.student')
    x_student=fields.Char(compute='_compute_depends')
  #  x_student = fields.many2one('op.student')#compute='_compute_depends')
   

##valor por default
 
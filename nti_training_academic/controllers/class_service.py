from odoo.addons.component.core import Component
from odoo.addons.base_rest import restapi
from datetime import datetime

class EmployeeService(Component):
    _inherit = 'base.rest.service'
    _name = 'class.service'
    _usage = 'class'
    _collection = 'base.rest.university.services'
    
    @restapi.method([(["/"], "POST")], auth="public", type="http",
    input_param=restapi.CerberusValidator("_create_class_schema"))
    def createClass(self, **params):
        params['date'] = datetime.strptime(params['date'], "%m/%d/%Y")
        new_class = self.env['class.class'].sudo().create(params)
        
        return {
            "status" : 200,
            "message" : "Success to Create Class",
            "result" : {
                "id" : new_class.id,
                "name" : new_class.name
            }
        }
        
    def _create_class_schema(self):
        return {
            'name': {'type': 'string', 'required': True},
            'date': {'type': 'string', 'required': True},
            'user_id': {'type': 'integer', 'required': True},
        }

    
    @restapi.method([(["/"], "GET")], auth="public",)
    def getAllClass(self):
        classes = self.env["class.class"].sudo().search([])
        result = []
        
        for kelas in classes:
            students = []
            subjects = []
            
            for student in kelas.student_ids:
                students.append({
                    "name" : student.name,
                    "phone" : student.phone,
                    "email" : student.email
                })
                
            for subject in kelas.subject_line_ids:
                subjects.append({
                    "subject" : subject.subject_id.name,
                    "lecturer" : subject.lecturer_id.name,
                    "start_hour" : subject.start_hour,
                    "end_hour" : subject.end_hour
                })
            
            result.append({
                "id" : kelas.id,
                "name" : kelas.name,
                "date" : kelas.date,
                "responsible" : kelas.user_id.name,
                "students" : students,
                "subjects" : subjects
            })
        
        return {"status": 200,
                "result": result}
        
    @restapi.method([(["/<int:id>"], "GET")], auth="public",)
    def getClassById(self, _id):
        kelas = self.env["class.class"].sudo().browse(_id)
        
        students = []
        subjects = []
        
        for student in kelas.student_ids:
            students.append({
                "name" : student.name,
                "phone" : student.phone,
                "email" : student.email
            })
            
        for subject in kelas.subject_line_ids:
            subjects.append({
                "subject" : subject.subject_id.name,
                "lecturer" : subject.lecturer_id.name,
                "start_hour" : subject.start_hour,
                "end_hour" : subject.end_hour
            })
        
        return {"status": 200,
                "result": {
                    "id" : kelas.id,
                    "name" : kelas.name,
                    "date" : kelas.date,
                    "responsible" : kelas.user_id.name,
                    "students" : students,
                    "subjects" : subjects
                }}
        
    @restapi.method([(["/<int:id>"], "PUT")], auth="public", type="http",
    input_param=restapi.CerberusValidator("_update_class_schema"))
    def updateClass(self, _id, **params):
        updated_employee = self.env['class.class'].sudo().browse(_id).write(params)
        return {
            "status" : 200,
            "message" : "Success to Update Employee"}
    
    def _update_class_schema(write):
        return {
            'name': {'type': 'string', 'required': False},
            'date': {'type': 'string', 'required': False},
            'user_id': {'type': 'integer', 'required': False},
        }
        
    @restapi.method([(["/<int:id>"], "DELETE")], auth="public",)
    def deleteClass(self, _id):
        updated_employee = self.env['class.class'].sudo().browse(_id).unlink()
        return {
            "status" : 200,
            "message" : "Success to Delete Class"}
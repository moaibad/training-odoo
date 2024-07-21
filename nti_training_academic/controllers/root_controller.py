from odoo.addons.base_rest.controllers import main

class RootController(main.RestController):
    _root_path = '/api/university/'
    _collection_name = 'base.rest.university.services'
    _default_auth = 'public'
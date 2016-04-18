# -*- coding: utf-8 -*-
# © 2015 Agile Business Group sagl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.addons.web.controllers.main import Binary
from openerp.addons.web import http
from openerp.addons.web.http import request
import openerp
from openerp.modules import get_module_resource
import functools
from cStringIO import StringIO

db_monodb = http.db_monodb


class website_logo(Binary):

    @http.route([
        '/website_logo.png',
    ], type='http', auth="none", cors="*")
    def website_logo(self, dbname=None, **kw):
        imgname = 'logo.png'
        uid = None
        if request.session.db:
            dbname = request.session.db
            uid = request.session.uid
        elif dbname is None:
            dbname = db_monodb()
        if not uid:
            uid = openerp.SUPERUSER_ID
        if uid and dbname:
            placeholder = functools.partial(
                get_module_resource, 'web', 'static', 'src', 'img')
            try:
                # create an empty registry
                registry = openerp.modules.registry.Registry(dbname)
                with registry.cursor() as cr:
                    cr.execute("""SELECT c.website_logo, c.write_date
                                    FROM res_users u
                               LEFT JOIN res_company c
                                      ON c.id = u.company_id
                                   WHERE u.id = %s
                               """, (uid,))
                    row = cr.fetchone()
                    if row and row[0]:
                        image_data = StringIO(str(row[0]).decode('base64'))
                        response = http.send_file(
                            image_data, filename=imgname, mtime=row[1])
                        return response
            except Exception:
                return http.send_file(placeholder(imgname))
        return super(website_logo, self).company_logo(dbname=dbname, **kw)

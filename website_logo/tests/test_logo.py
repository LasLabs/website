# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests import HttpCase
from openerp.addons.website_logo.controllers.main import WebsiteLogo
import mock


imp_cont = 'openerp.addons.website_logo.controllers.main'
imp_req = '%s.request' % imp_cont
mod_imp = '%s.Binary' % imp_cont


class TestLogo(HttpCase):

    @mock.patch(mod_imp)
    def setUp(self, mk):
        super(TestLogo, self).setUp()
        self.model_obj = self.env['res.company']
        self.cont_obj = WebsiteLogo()
        self.rec_id = self.env.ref('base.main_company')
        self.image_val = 'Test'.encode('base64')
        self.mock = mk

    @mock.patch('%s.http' % imp_cont)
    @mock.patch('%s.StringIO' % imp_cont)
    @mock.patch(imp_req)
    def test_sql_query_and_fetch(self, imp_mk, str_mk, http_mk):
        """ SQL query is executed and fetched """
        with mock.patch('%s.openerp' % imp_cont) as mk:
            cr_mk = mk.modules.registry.Registry().cursor().__enter__()
            self.cont_obj.website_logo()
            args = cr_mk.execute.call_args
            self.assertIn(
                'SELECT c.website_logo', args[0][0],
                'Website logo select not in query call',
            )

    @mock.patch('%s.http' % imp_cont)
    @mock.patch('%s.StringIO' % imp_cont)
    @mock.patch(imp_req)
    def test_packs_and_returns_file(self, imp_mk, str_mk, http_mk):
        """ Result of query is packed into StringIO then returned as file """
        with mock.patch('%s.openerp' % imp_cont) as mk:
            cr_mk = mk.modules.registry.Registry().cursor().__enter__()
            cr_mk.fetchone.return_value = [self.image_val, 123]
            res = self.cont_obj.website_logo()
            str_mk.assert_called_once_with(
                str(self.image_val).decode('base64')
            )
            http_mk.send_file.assert_called_once_with(
                str_mk(), filename='logo.png', mtime=123,
            )
            self.assertEqual(
                http_mk.send_file(), res,
                'Did not return image',
            )

    @mock.patch('%s.functools' % imp_cont)
    @mock.patch('%s.http' % imp_cont)
    @mock.patch('%s.StringIO' % imp_cont)
    @mock.patch(imp_req)
    def test_default_on_exception(self, imp_mk, str_mk, http_mk, func_mk):
        with mock.patch('%s.openerp' % imp_cont) as mk:
            cr_mk = mk.modules.registry.Registry().cursor().__enter__()
            cr_mk.execute.side_effect = StopIteration
            res = self.cont_obj.website_logo()
            http_mk.send_file.assert_called_once(func_mk())
            self.assertEqual(res, http_mk.send_file())

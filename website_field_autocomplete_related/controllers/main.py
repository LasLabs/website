# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from collections import defaultdict

from openerp import http
from openerp.addons.website_field_autocomplete.controllers.main import Website


class Website(Website):

    def _get_autocomplete_data(self, model, domain, fields, limit=None):
        """ Iterate dot notated field names and provide object """
        res = super(Website, self)._get_autocomplete_data(
            model, domain, fields, limit
        )
        for field in fields:
            if '.' in field:
                for rec_id in self.record_ids:
                    res[rec_id.id][field] = self._get_relation_data(
                        rec_id, field,
                    )
        return res

    def _get_relation_data(self, record_id, field_name):
        """ Iterate dot notated fields and inject data into object """
        obj = record_id
        for field_part in field_name.split('.'):
            obj = getattr(obj, field_part, None)
            if obj is None:
                return obj
        return obj

.. image:: https://img.shields.io/badge/license-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Website Field AutoComplete Related
==================================

Extends Website Autocomplete field to allow for related fields, for example
a form that automatically completes based on search results.

Usage
=====

To use this module, you would follow the instructions provided in
``website_field_autocomplete``.

The only difference is that you would create multiple auto complete
fields, then utilize the ``data-relate-group`` attribute to link the
fields' data & searches together.

If you would like to activate the relation on a non-autocomplete element,
you also need to add the ``data-query-field`` attribute or match the name of
the element to the name of the column.

Following is an example:

.. code:: xml

    <label for="name">Name</label>
    <input type="text"
           name="name"
           class="js_website_autocomplete"
           data-query-field="name"
           data-relate-group="res_partner"
           data-model="res.partner"
           />
    
    <label for="name">Phone</label>
    <input type="text"
           name="phone"
           class="js_website_autocomplete"
           data-query-field="phone"
           data-relate-group="res_partner"
           data-model="res.partner"
           />

    <label for="name">Company</label>
    <input type="text"
           name="company"
           data-query-field="street"
           data-relate-group="res_partner"
           />

    <label for="name">Street</label>
    <input type="text"
           name="street2"
           data-relate-group="res_partner"
           />


.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/186/9.0


Known Issues / Road Map
=======================


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/website/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.


Credits
=======

Contributors
------------

* Dave Lasley <dave@laslabs.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

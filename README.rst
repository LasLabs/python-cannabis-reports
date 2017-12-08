|License MIT| | |PyPi Package| | |PyPi Versions|

|Build Status| | |Test Coverage| | |Code Climate|

=======================
Python Cannabis Reports
=======================

This library allows you to interact with the Cannabis Reports API using Python.

* `Read The API Documentation <https://laslabs.github.io/python-cannabis-reports>`_

.. contents:: Table of Contents

============
Installation
============

Installation is easiest using Pip and PyPi::

   pip install cannabis-reports

If you would like to contribute, or prefer Git::

   git clone https://github.com/LasLabs/python-cannabis-reports.git
   cd python-cannabis-reports
   pip install .

=====
Usage
=====

The `CannabisReports object <https://laslabs.github.io/python-cannabis-reports/
cannabis-reports.html#cannabis-reports.CannabisReports>`_ is the primary point of
 interaction with the CannabisReports API.

Connection
==========

Connecting to the CannabisReports API will require an API Key, which is generated from
within your CannabisReports account. In the below example, our key is ``API_KEY``.

.. code-block:: python

   from cannabis-reports import CannabisReports
   cr = CannabisReports('API_KEY')

API Endpoints
=============

The CannabisReports API endpoints are exposed as variables on the instantiated 
``CannabisReports`` object. The available endpoints are:

* `Dispensaries <https://laslabs.github.io/python-cannabis-reports/
  cannabis-reports.apis.html#module-cannabis-reports.apis.dispensaries>`_
* `Edibles <https://laslabs.github.io/python-cannabis-reports/
  cannabis-reports.apis.html#module-cannabis-reports.apis.edibles>`_
* `Extracts <https://laslabs.github.io/python-cannabis-reports/
  cannabis-reports.apis.html#module-cannabis-reports.apis.extracts>`_
* `Flowers <https://laslabs.github.io/python-cannabis-reports/
  cannabis-reports.apis.html#module-cannabis-reports.apis.flowers>`_
* `Producers <https://laslabs.github.io/python-cannabis-reports/
  cannabis-reports.apis.html#module-cannabis-reports.apis.producers>`_
* `Products <https://laslabs.github.io/python-cannabis-reports/
  cannabis-reports.apis.html#module-cannabis-reports.apis.products>`_
* `Strains <https://laslabs.github.io/python-cannabis-reports/
  cannabis-reports.apis.html#module-cannabis-reports.apis.strains>`_

They can also be viewed from the ``__apis__`` property of ``CannabisReports``::

   >>> cr.__apis__
   {'Strains': <CannabisReports.auth_proxy.AuthProxy object at 0x10783ddd0>,
    }

API usage is as simple as calling the method with the required parameters and
iterating the results:

.. code-block:: python

   for strain in cr.Strains.list():
       print(strain)
       print(strain.serialize())
       break

The output from the above would look something like the below:

.. code-block:: python

   # This is the Strain object itself (first print)
   <cannabis-reports.models.strain.Strain object at 0x10783df10>
   # This is the serialized form of the Strain (second print)
   {'name': '#1K',
    'updated_at': {
        'datetime': '2015-06-16 22:10:20',
        'timezone': 'UTC'
    },
    'lineage': [],
    'qr': 'https://www.cannabisreports.com/strain-reports/unknown-breeder/1k/qr-code.svg',
    'seed_company': {
        '__class__': 'SeedCompany',
        'ucpc': '9XVU700000000000000000000',
        'link': 'https://www.cannabisreports.com/api/v1.0/seed-companies/9XVU700000000000000000000'
    },
    'genetics': {'__class__': 'StrainGenetics'},
    'created_at': {'datetime': '2015-06-16 22:10:20', 'timezone': 'UTC'},
    'reviews': {
        '__class__': 'GeneralOverview',
        'link': 'https://www.cannabisreports.com/api/v1.0/strains/9XVU7PZUEC000000000000000/reviews'
    },
    'image': 'https://www.cannabisreports.com/images/strains/no_image.png',
    'ucpc': '9XVU7PZUEC000000000000000',
    '__class__': 'Strain',
    'url': 'https://www.cannabisreports.com/strain-reports/unknown-breeder/1k',
    'children': {
        '__class__': 'GeneralOverview',
        'count': 2,
        'link': 'https://www.cannabisreports.com/api/v1.0/strains/9XVU7PZUEC000000000000000/children'
    },
    'link': 'https://www.cannabisreports.com/api/v1.0/strains/9XVU7PZUEC000000000000000'
   }

In some instances, such as in the case of browsing for a record by its UCPC, a
singleton is expected. In these instances, the singleton is directly used
instead of iterated

.. code-block:: python

   >>> strain = cr.Strains.get('9XVU7PZUEC000000000000000')
   >>> strain
   <cannabis-reports.models.strain.Strain object at 0x101723e50>
   >>> strain.serialize()
   {'name': '#1K',
    'updated_at': {
        'datetime': '2015-06-16 22:10:20',
        'timezone': 'UTC'
    },
    'lineage': [],
    'qr': 'https://www.cannabisreports.com/strain-reports/unknown-breeder/1k/qr-code.svg',
    'seed_company': {
        '__class__': 'SeedCompany',
        'ucpc': '9XVU700000000000000000000',
        'link': 'https://www.cannabisreports.com/api/v1.0/seed-companies/9XVU700000000000000000000'
    },
    'genetics': {'__class__': 'StrainGenetics'},
    'created_at': {'datetime': '2015-06-16 22:10:20', 'timezone': 'UTC'},
    'reviews': {
        '__class__': 'GeneralOverview',
        'link': 'https://www.cannabisreports.com/api/v1.0/strains/9XVU7PZUEC000000000000000/reviews'
    },
    'image': 'https://www.cannabisreports.com/images/strains/no_image.png',
    'ucpc': '9XVU7PZUEC000000000000000',
    '__class__': 'Strain',
    'url': 'https://www.cannabisreports.com/strain-reports/unknown-breeder/1k',
    'children': {
        '__class__': 'GeneralOverview',
        'count': 2,
        'link': 'https://www.cannabisreports.com/api/v1.0/strains/9XVU7PZUEC000000000000000/children'
    },
    'link': 'https://www.cannabisreports.com/api/v1.0/strains/9XVU7PZUEC000000000000000'
   }

Note that all of the API responses will be parsed, with proper objects being
created from the results. The objects are all defined in the `cannabis-reports.models
package <https://laslabs.github.io/python-cannabis-reports/cannabis-reports.models.html>`_.


Known Issues / Road Map
=======================

-  This ReadMe could use work
-  More testing on the endpoints. Kept getting rate limited and have not yet received
   and API key.

Credits
=======

Most of the doc strings were taken directly from the `Cannabis
Reports API Documentation <https://developers.cannabisreports.com/docs/>`_

Contributors
------------

* Dave Lasley <dave@laslabs.com>

Maintainer
----------

.. image:: https://laslabs.com/logo.png
   :alt: LasLabs Inc.
   :target: https://laslabs.com

This module is maintained by LasLabs Inc.

.. |Build Status| image:: https://img.shields.io/travis/LasLabs/python-cannabis-reports/master.svg
   :target: https://travis-ci.org/LasLabs/python-cannabis-reports
.. |Test Coverage| image:: https://img.shields.io/codecov/c/github/LasLabs/python-cannabis-reports/master.svg
   :target: https://codecov.io/gh/LasLabs/python-cannabis-reports
.. |Code Climate| image:: https://codeclimate.com/github/LasLabs/python-cannabis-reports/badges/gpa.svg
   :target: https://codeclimate.com/github/LasLabs/python-cannabis-reports
.. |License MIT| image:: https://img.shields.io/github/license/laslabs/python-cannabis-reports.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT
.. |PyPi Package| image:: https://img.shields.io/pypi/v/cannabis-reports.svg
   :target: https://pypi.python.org/pypi/cannabis-reports
   :alt: PyPi Package
.. |PyPi Versions| image:: https://img.shields.io/pypi/pyversions/cannabis-reports.svg
   :target: https://pypi.python.org/pypi/cannabis-reports
   :alt: PyPi Versions

.. _services:

Services
========

wis2box provides a number of data access services and mechanisms in providing data
to users, applications and beyond.

Discovery Catalogue
-------------------

The discovery catalogue is powered by `OGC API - Records`_ and is located at http://localhost:8999/oapi/collections/discovery-metadata

The OGC API endpoint is located by default at http://localhost:8999/oapi.  The discovery catalogue endpoint is located at http://localhost:8999/oapi/collections/discovery-metadata

Below are some examples of working with the discovery catalogue.

- description of catalogue: http://localhost:8999/oapi/collections/discovery-metadata
- catalogue queryables: http://localhost:8999/oapi/collections/discovery-metadata/queryables
- catalogue queries

  - records (browse): http://localhost:8999/oapi/collections/discovery-metadata/items
  - query by spatial (bounding box): http://localhost:8999/oapi/collections/discovery-metadata/items?bbox=32,-17,36,-8
  - query by temporal extent (since): http://localhost:8999/oapi/collections/discovery-metadata/items?datetime=2021/..
  - query by temporal extent (before): http://localhost:8999/oapi/collections/discovery-metadata/items?datetime=../2022
  - query by freetext: http://localhost:8999/oapi/collections/discovery-metadata/items?q=observations

.. note::

   - adding ``f=json`` to URLs will provide the equivalent JSON/GeoJSON representations
   - query predicates (``datetime``, ``bbox``, ``q``, etc.) can be combined

.. seealso:: :ref:`data-access`


Data API
--------

wis2box data is made available via `OGC API - Features`_ and is located at http://localhost:8999/oapi
standards.

The OGC API endpoint is located by default at http://localhost:8999/oapi

Below are some examples of working with the discovery catalogue.

.. note::

   - the examples below use the ``data.core.observations-surface-land.mw.FWCL.landFixed`` collection as described
     in the :ref:`quickstart`.  For other dataset collections, use the same query patterns below, substituting the
     collection id accordingly


- list of dataset collections: http://localhost:8999/oapi/collections
- collection description: http://localhost:8999/oapi/collections/data.core.observations-surface-land.mw.FWCL.landFixed
- collection queryables: http://localhost:8999/oapi/collections/data.core.observations-surface-land.mw.FWCL.landFixed/queryables
- collection items (browse): http://localhost:8999/oapi/collections/data.core.observations-surface-land.mw.FWCL.landFixed/items
- collection queries

  - set limit/offset (paging): http://localhost:8999/oapi/collections/data.core.observations-surface-land.mw.FWCL.landFixed/items?limit=1&startindex=2
  - query by spatial (bounding box): http://localhost:8999/oapi/collections/data.core.observations-surface-land.mw.FWCL.landFixed/items?bbox=32,-17,36,-8
  - query by temporal extent (since): http://localhost:8999/oapi/collections/data.core.observations-surface-land.mw.FWCL.landFixed/items?datetime=2021/..
  - query by temporal extent (before): http://localhost:8999/oapi/collections/data.core.observations-surface-land.mw.FWCL.landFixed/items?datetime=../2022

.. note::

   - adding ``f=json`` to URLs will provide the equivalent JSON/GeoJSON representations
   - query predicates (``datetime``, ``bbox``, ``q``, etc.) can be combined

.. seealso:: :ref:`data-access`


SpatioTemporal Asset Catalog (STAC)
-----------------------------------

The wis2box `SpatioTemporal Asset Catalog (STAC)`_ endpoint can be found at:

http://localhost:8999/stac

...providing the user with a crawlable catalogue of all data on a wis2box.


Web Accessible Folder (WAF)
----------------------------

The wis2box `SpatioTemporal Asset Catalog (STAC)`_ endpoint can be found at:

http://localhost:8999/data/

...providing the user with a crawlable online folder of all data on a wis2box.


Broker
------

The wis2box broker is powered by `MQTT`_ and can be found at:

mqtt://localhost:1883

...providing a PubSub capability for event driven subscription and access.


Adding services
---------------

wis2box's architecture allows for additional services as required by
adding Docker containers. Examples of additional services include adding a container
for a samba share or FTP server. Key considerations for adding services:

- volume mapping data directories: all wis2box data can be found at ``${WIS2BOX_DATADIR}``
  - incoming: ``${WIS2BOX_DATADIR}/data/incoming``
  - public: ``${WIS2BOX_DATADIR}/data/public``
- Elasticsearch indexes can be found at the container/URL ``http://elasticsearch:9200``

Examples of additional services can be found in ``docker/extras``.


.. _`OGC API - Features`: https://ogcapi.ogc.org/features
.. _`OGC API - Records`: https://ogcapi.ogc.org/records
.. _`SpatioTemporal Asset Catalog (STAC)`: https://stacspec.org
.. _`MQTT`: https://mqtt.org

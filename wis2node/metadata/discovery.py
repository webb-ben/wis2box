###############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
###############################################################################

import click
import logging

from pygeometa.schemas.ogcapi_records import OGCAPIRecordOutputSchema

from wis2node import cli_helpers
from wis2node.catalogue import delete_metadata
from wis2node.metadata.base import MetadataBase

LOGGER = logging.getLogger(__name__)


class DiscoveryMetadata(MetadataBase):
    def __init__(self):
        super().__init__()

    def generate(mcf: dict) -> dict:
        """
        Generate OARec discovery metadata

        :param mcf: `dict` of MCF file

        :returns: `dict` of metadata representation
        """

        LOGGER.debug('Generating OARec discovery metadata')
        return OGCAPIRecordOutputSchema().write(mcf)


@click.group()
def discovery():
    """Discovery metadata management"""
    pass


@click.command()
@click.pass_context
@cli_helpers.ARGUMENT_FILEPATH
@cli_helpers.OPTION_VERBOSITY
def publish(ctx, filepath, verbosity):
    """Inserts or updates discovery metadata to catalogue"""

    try:
        record = DiscoveryMetadata().parse_record(filepath.read())
        discovery.upsert_metadata(record.generate(record))
    except Exception as err:
        raise click.ClickException(err)

    click.echo('Done')


@click.command()
@click.pass_context
@click.argument('identifier')
def unpublish(ctx, identifier):
    """Deletes a discovery metadata record from the catalogue"""

    delete_metadata(identifier)


discovery.add_command(publish)
discovery.add_command(unpublish)
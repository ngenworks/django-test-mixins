"""
Nose plugins
"""

import logging
from nose.plugins import Plugin


class SuppressSouth(Plugin):
    """
    Suppress South logging levels
    """
    south_logging_level = logging.ERROR

    def configure(self, options, conf):
        super(SuppressSouth, self).configure(options, conf)
        logging.getLogger('south').setLevel(self.south_logging_level)

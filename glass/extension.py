# author: Author Name <author_email@example.com>
# license: MIT
'''GLASS module for extension'''

__version__ = '2022.3.14'


import logging
# non-GLASS imports

from glass.core import generator
# other GLASS imports (don't forget to add requirements if extensions)


log = logging.getLogger(__name__)


@generator('zmin, zmax -> zmean')
def zmean():
    '''generator for mean redshift'''

    zmean = None

    while True:
        try:
            zmin, zmax = yield zmean
        except GeneratorExit:
            break

        zmean = (zmin + zmax)/2

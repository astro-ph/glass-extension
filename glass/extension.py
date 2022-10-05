# author: Author Name <author_email@example.com>
# license: MIT
'''GLASS module for extension'''

__version__ = '2022.10.5'


# non-GLASS imports
import logging

from glass.generator import generator
from glass.sim import ZMIN, ZMAX
# ... other GLASS imports (don't forget to add requirements if extensions)

logger = logging.getLogger(__name__)

# variable definitions
ZMEAN = 'mean redshift of matter shell'
'''An example variable for the mean redshift of the matter shell.'''


@generator(
    receives=(ZMIN, ZMAX),
    yields=ZMEAN)
def zmean():
    '''example generator for the mean redshift'''

    zmean = None

    while True:
        zmin, zmax = yield zmean

        zmean = (zmin + zmax)/2

        logger.info('mean redshift: %.3f', zmean)

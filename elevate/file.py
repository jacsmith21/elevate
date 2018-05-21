import os
import sys

import requests

from elevate import pylog

LOGGER = pylog.get_logger(__name__)


def download(url, dst):
    """
    Downloads a file from a url to the given destination with % finished bar.
    :param url: The url.
    :param dst: The destination.
    """
    if os.path.isfile(dst):
        return

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        LOGGER.info('Downloading %s to %s' % (url, dst))
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()

from collections import defaultdict
from functools import partial
import logging
import random

from mlabns.db import model
from mlabns.util import constants
from mlabns.util import message

from google.appengine.api import memcache

class ClientSignatureFetcher(object):
    """fetch probability of matched client signature from AppEngine memcache."""        

    def fetch(self, key):
        """Fetch probability of matched client signature.        

        Args:
            key: A string in format like:
                 'name=127.0.0.1#userAgent#/ndt_ssl?policy=geo_options'

        Returns:
            The probability of matched client signature or 0 if there is no
            matched entry.
        """
        matched_requests = memcache.get(
            client_signature,
            namespace=constants.MEMCACHE_NAMESPACE_REQUESTS)
        if matched_requests and len(matched_requests) == 1:
            return matched_requests[0].probability
        return 0
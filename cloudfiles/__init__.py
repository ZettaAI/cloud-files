"""
CloudFiles is a multithreaded key-value object
management client that supports GET, PUT, DELETE,
EXISTS, and LIST operations.

It can support any key-value storage system and 
currently supports local filesystem, Google Cloud Storage,
Amazon S3 interfaces, and reading from arbitrary HTTP 
servers.
"""
__version__ = '1.25.dev1'

from .cloudfiles import CloudFiles, dl
from .interfaces import reset_connection_pools
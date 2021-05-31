from shutil import copyfile
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import\
    DriverRemoteConnection
import os


class RemoteGremlin(object):
    def __init__(self, server, port=8182):
        '''
        construct me with the given server and port
        '''
        self.server = server
        self.port = port

    def sharepoint(self, sharepoint, sharepath):
        '''
        set up the sharepoint
        '''
        self.sharepoint = sharepoint
        self.sharepath = sharepath

    def share(self, file):
        '''
        share the given file  and return the path as seen by the server
        '''
        fbase = os.path.basename(file)
        copyfile(file, self.sharepoint+fbase)
        return self.sharepath+fbase

    def open(self):
        '''
        open the remote connection
        '''
        self.url = 'ws://%s:%s/gremlin' % (self.server, self.port)
        self.connection = DriverRemoteConnection(self.url, 'g')
        # The connection should be closed on shut down to close open
        # connections with connection.close()
        self.g = traversal().withRemote(self.connection)

    def close(self):
        '''
        close the remote connection
        '''
        self.connection.close()

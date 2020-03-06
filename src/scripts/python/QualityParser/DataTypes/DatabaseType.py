#! /usr/bin/env python2.7

class DatabaseType(object):
    def toDatabaseEntry(self):
        raise NotImplementedError


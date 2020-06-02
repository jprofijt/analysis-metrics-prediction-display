#! /usr/bin/env python2.7

class DatabaseType(object):
    """Each Database type must have a toDatabase entry function which formats the data to the database format"""
    def toDatabaseEntry(self):
         """Should format the information stored in the database type to an actual database type

            Returns:
            Database entry (Tuple): Tuple of values to add to database

        """
        raise NotImplementedError


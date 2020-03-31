#! /usr/bin/env python2

from __future__ import absolute_import
from .DatabaseType import DatabaseType

class Summary(DatabaseType):
    def __init__(self, Run, Flowcell, Yield, Projected, Aligned, ErrorRate, Intencity, Q30):
        self.Run = Run,
        self.Yield = Yield,
        self.Projected = Projected,
        self.Aligned = Aligned,
        self.ErrorRate = ErrorRate,
        self.Intencity = Intencity,
        self.Q30 = Q30
        
    def toDatabaseEntry(self):
        return (
            self.Run,
            self.Yield,
            self.Projected,
            self.Aligned,
            self.ErrorRate,
            self.Intencity,
            self.Q30
        )


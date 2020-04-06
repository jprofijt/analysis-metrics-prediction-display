#! /usr/bin/env python2.7

from .DatabaseType import DatabaseType

class Lane(DatabaseType):
    def __init__(
        self,ReadID,Lane,
        Tiles,DensityMIN,DensityMAX,ClusterMIN,
        ClusterMAX,LegacyPhasing,LegacyPrePhasing,PhasingSlope,
        PhasingOffset,PrePhasingSlope,PrePhasingOffset,Reads,
        ReadsPF,Q30,IntensityMIN,IntensityMAX):
        self.ReadID = ReadID
        self.Lane = Lane
        self.Tiles = Tiles
        self.DensityMIN = DensityMIN
        self.DensityMAX = DensityMAX
        self.ClusterMIN = ClusterMIN
        self.ClusterMAX = ClusterMAX
        self.LegacyPhasing = LegacyPhasing
        self.LegacyPrePhasing = LegacyPrePhasing
        self.PhasingSlope = PhasingSlope
        self.PhasingOffset = PhasingOffset
        self.PrePhasingSlope = PrePhasingSlope
        self.PrePhasingOffset = PrePhasingOffset
        self.Reads = Reads
        self.ReadsPF = ReadsPF
        self.Q30 = Q30
        self.IntensityMIN = IntensityMIN
        self.IntensityMAX = IntensityMAX
    
    def toDatabaseEntry(self):
        return (
            self.ReadID,
            self.Lane,
            self.Tiles,
            self.DensityMIN,
            self.DensityMAX,
            self.ClusterMIN,
            self.ClusterMAX,
            self.LegacyPhasing,
            self.LegacyPrePhasing,
            self.PhasingSlope,
            self.PhasingOffset,
            self.PrePhasingSlope,
            self.PrePhasingOffset,
            self.Reads,
            self.ReadsPF,
            self.Q30,
            self.IntensityMIN,
            self.IntensityMAX
        )
        
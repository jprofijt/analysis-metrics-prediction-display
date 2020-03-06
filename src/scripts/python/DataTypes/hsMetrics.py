#! /usr/bin/env python2.7
# pylint: disable=relative-beyond-top-level

from .DatabaseType import DatabaseType

class hsMetric(DatabaseType):
    def __init__(self, SampleID, RunID, BaitSet, GenomeSize , BaitTerritory , TargetTerritory , BaitDesignEfficientcy , TotalReads , PFreads , PFuniqueReads , PFUQaligned , PFBasesAligned , PFUQBasesAligned , OnBaitBases , NearBaitBases , OffBaitBases , OnTargetBases , SelectedBasesPercentage , OnBaitVSselected , MeanBaitCoverage , MeanTargetCoverage , MedianTargetCoverage, PercentageUsableBasesOnBait , PercentageUsableBasesOnTarget , FoldEnrichment , ZeroCVGtargetsPercentage , ExcDupePct , ExcMapQPct , ExcBaseQPct , ExcOverlapPct , ExcOffTargetPct , Fold80BasePenalty , TargetBasesPct1X , TargetBasesPct2X , TargetBasesPct10X , TargetBasesPct20X , TargetBasesPct30X , TargetBasesPct40X , TargetBasesPct50X , TargetBasesPct100X , HsLibrarySize , HsPenalty10X , HsPenalty20X , HsPenalty30X, HsPenalty40X, HsPenalty50X , HsPenalty100X , AtDropout , GCDropout , HetSNPsensitivity , HetSNPQ ):
        self.SampleID = str(SampleID)
        self.RunID = str(RunID)
        self.BaitSet = str(BaitSet)
        self.GenomeSize  = str(GenomeSize) 
        self.BaitTerritory  = str(BaitTerritory) 
        self.TargetTerritory  = str(TargetTerritory) 
        self.BaitDesignEfficientcy  = str(BaitDesignEfficientcy) 
        self.TotalReads  = str(TotalReads) 
        self.PFreads  = str(PFreads) 
        self.PFuniqueReads  = str(PFuniqueReads) 
        self.PFUQaligned  = str(PFUQaligned) 
        self.PFBasesAligned  = str(PFBasesAligned) 
        self.PFUQBasesAligned  = str(PFUQBasesAligned) 
        self.OnBaitBases  = str(OnBaitBases) 
        self.NearBaitBases  = str(NearBaitBases) 
        self.OffBaitBases  = str(OffBaitBases) 
        self.OnTargetBases  = str(OnTargetBases) 
        self.SelectedBasesPercentage  = str(SelectedBasesPercentage) 
        self.OnBaitVSselected  = str(OnBaitVSselected) 
        self.MeanBaitCoverage  = str(MeanBaitCoverage) 
        self.MeanTargetCoverage  = str(MeanTargetCoverage) 
        self.MedianTargetCoverage = str(MedianTargetCoverage)
        self.PercentageUsableBasesOnBait  = str(PercentageUsableBasesOnBait) 
        self.PercentageUsableBasesOnTarget  = str(PercentageUsableBasesOnTarget) 
        self.FoldEnrichment  = str(FoldEnrichment) 
        self.ZeroCVGtargetsPercentage  = str(ZeroCVGtargetsPercentage) 
        self.ExcDupePct  = str(ExcDupePct) 
        self.ExcMapQPct  = str(ExcMapQPct) 
        self.ExcBaseQPct  = str(ExcBaseQPct) 
        self.ExcOverlapPct  = str(ExcOverlapPct) 
        self.ExcOffTargetPct  = str(ExcOffTargetPct) 
        self.Fold80BasePenalty  = str(Fold80BasePenalty) 
        self.TargetBasesPct1X  = str(TargetBasesPct1X) 
        self.TargetBasesPct2X  = str(TargetBasesPct2X) 
        self.TargetBasesPct10X  = str(TargetBasesPct10X) 
        self.TargetBasesPct20X  = str(TargetBasesPct20X) 
        self.TargetBasesPct30X  = str(TargetBasesPct30X) 
        self.TargetBasesPct40X  = str(TargetBasesPct40X) 
        self.TargetBasesPct50X  = str(TargetBasesPct50X) 
        self.TargetBasesPct100X  = str(TargetBasesPct100X) 
        self.HsLibrarySize  = str(HsLibrarySize) 
        self.HsPenalty10X  = str(HsPenalty10X) 
        self.HsPenalty20X  = str(HsPenalty20X) 
        self.HsPenalty30X  = str(HsPenalty30X) 
        self.HsPenalty40X  = str(HsPenalty40X) 
        self.HsPenalty50X  = str(HsPenalty50X) 
        self.HsPenalty100X  = str(HsPenalty100X) 
        self.AtDropout  = str(AtDropout) 
        self.GCDropout  = str(GCDropout) 
        self.HetSNPsensitivity  = str(HetSNPsensitivity) 
        self.HetSNPQ = str(HetSNPQ) 
    
    def toDatabaseEntry(self):
        return ( 
            self.SampleID, 
            self.RunID, 
            self.BaitSet, 
            self.GenomeSize,  
            self.BaitTerritory,  
            self.TargetTerritory,  
            self.BaitDesignEfficientcy,  
            self.TotalReads,  
            self.PFreads,  
            self.PFuniqueReads,  
            self.PFUQaligned,  
            self.PFBasesAligned,  
            self.PFUQBasesAligned,  
            self.OnBaitBases,  
            self.NearBaitBases,  
            self.OffBaitBases,  
            self.OnTargetBases,  
            self.SelectedBasesPercentage,  
            self.OnBaitVSselected,  
            self.MeanBaitCoverage,  
            self.MeanTargetCoverage,  
            self.MedianTargetCoverage, 
            self.PercentageUsableBasesOnBait,  
            self.PercentageUsableBasesOnTarget,  
            self.FoldEnrichment,  
            self.ZeroCVGtargetsPercentage,  
            self.ExcDupePct,  
            self.ExcMapQPct,  
            self.ExcBaseQPct,  
            self.ExcOverlapPct,  
            self.ExcOffTargetPct,  
            self.Fold80BasePenalty,  
            self.TargetBasesPct1X,  
            self.TargetBasesPct2X,  
            self.TargetBasesPct10X,  
            self.TargetBasesPct20X,  
            self.TargetBasesPct30X,  
            self.TargetBasesPct40X,  
            self.TargetBasesPct50X,  
            self.TargetBasesPct100X,  
            self.HsLibrarySize,  
            self.HsPenalty10X,  
            self.HsPenalty20X,  
            self.HsPenalty30X,  
            self.HsPenalty40X,  
            self.HsPenalty50X,  
            self.HsPenalty100X,  
            self.AtDropout,  
            self.GCDropout,  
            self.HetSNPsensitivity,  
            self.HetSNPQ 
        )

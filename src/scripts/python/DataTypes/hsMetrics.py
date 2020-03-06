class hsMetric(object):
    def __init__(self, SampleID, RunID, BaitSet, GenomeSize , BaitTerritory , TargetTerritory , BaitDesignEfficientcy , TotalReads , PFreads , PFuniqueReads , PFUQaligned , PFBasesAligned , PFUQBasesAligned , OnBaitBases , NearBaitBases , OffBaitBases , OnTargetBases , SelectedBasesPercentage , OnBaitVSselected , MeanBaitCoverage , MeanTargetCoverage , MedianTargetCoverage, PercentageUsableBasesOnBait , PercentageUsableBasesOnTarget , FoldEnrichment , ZeroCVGtargetsPercentage , ExcDupePct , ExcMapQPct , ExcBaseQPct , ExcOverlapPct , ExcOffTargetPct , Fold80BasePenalty , TargetBasesPct1X , TargetBasesPct2X , TargetBasesPct10X , TargetBasesPct20X , TargetBasesPct30X , TargetBasesPct40X , TargetBasesPct50X , TargetBasesPct100X , HsLibrarySize , HsPenalty10X , HsPenalty20X , HsPenalty30X, HsPenalty40X, HsPenalty50X , HsPenalty100X , AtDropout , GCDropout , HetSNPsensitivity , HetSNPQ ):
        self.SampleID = SampleID
        self.RunID = RunID
        self.BaitSet = BaitSet
        self.GenomeSize  = GenomeSize 
        self.BaitTerritory  = BaitTerritory 
        self.TargetTerritory  = TargetTerritory 
        self.BaitDesignEfficientcy  = BaitDesignEfficientcy 
        self.TotalReads  = TotalReads 
        self.PFreads  = PFreads 
        self.PFuniqueReads  = PFuniqueReads 
        self.PFUQaligned  = PFUQaligned 
        self.PFBasesAligned  = PFBasesAligned 
        self.PFUQBasesAligned  = PFUQBasesAligned 
        self.OnBaitBases  = OnBaitBases 
        self.NearBaitBases  = NearBaitBases 
        self.OffBaitBases  = OffBaitBases 
        self.OnTargetBases  = OnTargetBases 
        self.SelectedBasesPercentage  = SelectedBasesPercentage 
        self.OnBaitVSselected  = OnBaitVSselected 
        self.MeanBaitCoverage  = MeanBaitCoverage 
        self.MeanTargetCoverage  = MeanTargetCoverage 
        self.MedianTargetCoverage = MedianTargetCoverage
        self.PercentageUsableBasesOnBait  = PercentageUsableBasesOnBait 
        self.PercentageUsableBasesOnTarget  = PercentageUsableBasesOnTarget 
        self.FoldEnrichment  = FoldEnrichment 
        self.ZeroCVGtargetsPercentage  = ZeroCVGtargetsPercentage 
        self.ExcDupePct  = ExcDupePct 
        self.ExcMapQPct  = ExcMapQPct 
        self.ExcBaseQPct  = ExcBaseQPct 
        self.ExcOverlapPct  = ExcOverlapPct 
        self.ExcOffTargetPct  = ExcOffTargetPct 
        self.Fold80BasePenalty  = Fold80BasePenalty 
        self.TargetBasesPct1X  = TargetBasesPct1X 
        self.TargetBasesPct2X  = TargetBasesPct2X 
        self.TargetBasesPct10X  = TargetBasesPct10X 
        self.TargetBasesPct20X  = TargetBasesPct20X 
        self.TargetBasesPct30X  = TargetBasesPct30X 
        self.TargetBasesPct40X  = TargetBasesPct40X 
        self.TargetBasesPct50X  = TargetBasesPct50X 
        self.TargetBasesPct100X  = TargetBasesPct100X 
        self.HsLibrarySize  = HsLibrarySize 
        self.HsPenalty10X  = HsPenalty10X 
        self.HsPenalty20X  = HsPenalty20X 
        self.HsPenalty30X  = HsPenalty30X 
        self.HsPenalty40X  = HsPenalty40X 
        self.HsPenalty50X  = HsPenalty50X 
        self.HsPenalty100X  = HsPenalty100X 
        self.AtDropout  = AtDropout 
        self.GCDropout  = GCDropout 
        self.HetSNPsensitivity  = HetSNPsensitivity 
        self.HetSNPQ = HetSNPQ 
    
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

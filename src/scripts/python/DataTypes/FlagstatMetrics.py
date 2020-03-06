class FlagstatMetric(object):
    def __init__(self, SampleID, RunID,TotalPass,TotalFail,SecondaryPass,SecondaryFail,SupplementaryPass,SupplementaryFail,DuplicatePass,DuplicateFail,MappedPass,MappedFail,MappedPercentage ,PairedSeqPass,PairedSeqFail,Read1Pass,Read1Fail,Read2Pass,Read2Fail,PoperPairPass,ProperPairFail,SingletonsPass,SingletonsFail,SingletonsPercentage ,MateOnDiffChromosomeLowPass,MateOnDiffChromosomeLowFail,MateOnDiffChromosomeHighPass,MateOnDiffChromosomeHighFail):
        self.SampleID = SampleID  
        self.RunID = RunID  
        self.TotalPass = TotalPass
        self.TotalFail = TotalFail
        self.SecondaryPass = SecondaryPass
        self.SecondaryFail = SecondaryFail
        self.SupplementaryPass = SupplementaryPass
        self.SupplementaryFail = SupplementaryFail
        self.DuplicatePass = DuplicatePass
        self.DuplicateFail = DuplicateFail
        self.MappedPass = MappedPass
        self.MappedFail = MappedFail
        self.MappedPercentage = MappedPercentage
        self.PairedSeqPass = PairedSeqPass
        self.PairedSeqFail = PairedSeqFail
        self.Read1Pass = Read1Pass
        self.Read1Fail = Read1Fail
        self.Read2Pass = Read2Pass
        self.Read2Fail = Read2Fail
        self.PoperPairPass = PoperPairPass
        self.ProperPairFail = ProperPairFail
        self.SingletonsPass = SingletonsPass
        self.SingletonsFail = SingletonsFail
        self.SingletonsPercentage = SingletonsPercentage
        self.MateOnDiffChromosomeLowPass = MateOnDiffChromosomeLowPass
        self.MateOnDiffChromosomeLowFail = MateOnDiffChromosomeLowFail
        self.MateOnDiffChromosomeHighPass = MateOnDiffChromosomeHighPass
        self.MateOnDiffChromosomeHighFail = MateOnDiffChromosomeHighFail

    def toDatabaseEntry(self):
        return (
            self.SampleID,
            self.RunID,
            self.TotalPass,
            self.TotalFail,
            self.SecondaryPass,
            self.SecondaryFail,
            self.SupplementaryPass,
            self.SupplementaryFail,
            self.DuplicatePass,
            self.DuplicateFail,
            self.MappedPass,
            self.MappedFail,
            self.MappedPercentage,
            self.PairedSeqPass,
            self.PairedSeqFail,
            self.Read1Pass,
            self.Read1Fail,
            self.Read2Pass,
            self.Read2Fail,
            self.PoperPairPass,
            self.ProperPairFail,
            self.SingletonsPass,
            self.SingletonsFail,
            self.SingletonsPercentage,
            self.MateOnDiffChromosomeLowPass,
            self.MateOnDiffChromosomeLowFail,
            self.MateOnDiffChromosomeHighPass,
            self.MateOnDiffChromosomeHighFail
        )

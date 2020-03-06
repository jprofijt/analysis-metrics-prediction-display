#! /usr/bin/env python2.7
# pylint: disable=relative-beyond-top-level

from .DatabaseType import DatabaseType

class FlagstatMetric(DatabaseType):
    def __init__(self, SampleID, RunID,TotalPass,TotalFail,SecondaryPass,SecondaryFail,SupplementaryPass,SupplementaryFail,DuplicatePass,DuplicateFail,MappedPass,MappedFail,MappedPercentage ,PairedSeqPass,PairedSeqFail,Read1Pass,Read1Fail,Read2Pass,Read2Fail,PoperPairPass,ProperPairFail,SingletonsPass,SingletonsFail,SingletonsPercentage ,MateOnDiffChromosomeLowPass,MateOnDiffChromosomeLowFail,MateOnDiffChromosomeHighPass,MateOnDiffChromosomeHighFail):
        self.SampleID = str(SampleID)  
        self.RunID = str(RunID)  
        self.TotalPass = str(TotalPass)
        self.TotalFail = str(TotalFail)
        self.SecondaryPass = str(SecondaryPass)
        self.SecondaryFail = str(SecondaryFail)
        self.SupplementaryPass = str(SupplementaryPass)
        self.SupplementaryFail = str(SupplementaryFail)
        self.DuplicatePass = str(DuplicatePass)
        self.DuplicateFail = str(DuplicateFail)
        self.MappedPass = str(MappedPass)
        self.MappedFail = str(MappedFail)
        self.MappedPercentage = str(MappedPercentage)
        self.PairedSeqPass = str(PairedSeqPass)
        self.PairedSeqFail = str(PairedSeqFail)
        self.Read1Pass = str(Read1Pass)
        self.Read1Fail = str(Read1Fail)
        self.Read2Pass = str(Read2Pass)
        self.Read2Fail = str(Read2Fail)
        self.PoperPairPass = str(PoperPairPass)
        self.ProperPairFail = str(ProperPairFail)
        self.SingletonsPass = str(SingletonsPass)
        self.SingletonsFail = str(SingletonsFail)
        self.SingletonsPercentage = str(SingletonsPercentage)
        self.MateOnDiffChromosomeLowPass = str(MateOnDiffChromosomeLowPass)
        self.MateOnDiffChromosomeLowFail = str(MateOnDiffChromosomeLowFail)
        self.MateOnDiffChromosomeHighPass = str(MateOnDiffChromosomeHighPass)
        self.MateOnDiffChromosomeHighFail = str(MateOnDiffChromosomeHighFail)

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

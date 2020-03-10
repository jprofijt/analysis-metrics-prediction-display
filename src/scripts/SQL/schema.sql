DROP TABLE IF EXISTS FlagstatMetrics;
DROP TABLE IF EXISTS hsMetrics;
DROP TABLE IF EXISTS GCBiasMetrics;
DROP TABLE IF EXISTS AlignmentSummaryMetrics;
DROP TABLE IF EXISTS InsertSizes;
DROP TABLE IF EXISTS QualityByCycle;
DROP TABLE IF EXISTS QualityDistributions;
DROP TABLE IF EXISTS Samples;
DROP TABLE IF EXISTS CapturingKits;
DROP TABLE IF EXISTS Sequencers;
DROP TABLE IF EXISTS Projects;

CREATE TABLE Projects (
    ID TEXT NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE Sequencers (
    ID TEXT NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE Capturingkits (
    ID TEXT NOT NULL,
    startUsageDate DATE,
    endUsageDate DATE,
    PRIMARY KEY (ID)
);

CREATE TABLE Samples (
    ID TEXT NOT NULL UNIQUE,
    Sequencer TEXT NOT NULL,
    run INT NOT NULL,
    flowcell TEXT NOT NULL,
    startDate DATE NOT NULL,
    project TEXT NOT NULL,
    capturingKit TEXT NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (sequencer) REFERENCES Sequencers(ID),
    FOREIGN KEY (project) REFERENCES Projects(ID),
    FOREIGN KEY (capturingKit) REFERENCES CapturingKits(ID)
);

CREATE TABLE QualityDistributions (
    SampleID TEXT NOT NULL,
    bin INT NOT NULL,
    Qcount INT NOT NULL,
    FOREIGN KEY (SampleID) REFERENCES Samples(ID)
);

CREATE TABLE QualityByCycle (
    SampleID TEXT NOT NULL,
    runID TEXT NOT NULL,
    Cycle INT NOT NULL,
    Quality FLOAT NOT NULL,
    PRIMARY KEY (SampleID, runID, Cycle),
    FOREIGN KEY (SampleID) REFERENCES Samples(ID)
);

CREATE TABLE InsertSizes (
    SampleID TEXT NOT NULL,
    RunID TEXT NOT NULL,
    MedianSize INT NOT NULL,
    MedianAbsoluteDeviation INT NOT NULL,
    MinSize INT NOT NULL,
    MaxSize INT NOT NULL,
    MeanSize INT NOT NULL,
    StandardDeviation FLOAT NOT NULL,
    ReadPairs INT NOT NULL,
    PairOrientation TEXT NOT NULL,
    W10 INT NOT NULL,
    W20 INT NOT NULL,
    W30 INT NOT NULL,
    W40 INT NOT NULL,
    W50 INT NOT NULL,
    W60 INT NOT NULL,
    W70 INT NOT NULL,
    W80 INT NOT NULL,
    W90 INT NOT NULL,
    W99 INT NOT NULL,
    PRIMARY KEY (SampleID, RunID),
    FOREIGN KEY (SampleID) REFERENCES Samples(ID)
);

CREATE TABLE AlignmentSummaryMetrics (
    SampleID TEXT NOT NULL,
    RunID TEXT NOT NULL,
    Category TEXT NOT NULL,
    TotalReads INT NOT NULL,
    PFreads INT NOT NULL,
    PFnoise INT NOT NULL,
    PFaligned INT NOT NULL,
    PFHQaligned INT NOT NULL,
    PFalignedBases INT NOT NULL,
    PFHQalignedBases INT NOT NULL,
    PFHQalignedQ20Bases INT NOT NULL,
    PFHQmedianMismatches INT NOT NULL,
    PFmismatchRate FLOAT NOT NULL,
    PFHQErrorRate FLOAT NOT NULL,
    PFindelRate FLOAT NOT NULL,
    MeanReadLenght FLOAT NOT NULL,
    ReadsAllignedInPairs INT NOT NULL,
    BadCycles INT NOT NULL,
    StrandBalance FLOAT NOT NULL,
    ChimerasPercentage FLOAT NOT NULL,
    AdapterPercentage FLOAT NOT NULL,
    PRIMARY KEY (SampleID, RunID, Category),
    FOREIGN KEY (SampleID) REFERENCES Samples(ID)
);


CREATE TABLE GCBiasMetrics (
    SampleID TEXT NOT NULL,
    RunID TEXT NOT NULL,
    AccumilationLevel TEXT NOT NULL,
    ReadsUsed TEXT NOT NULL,
    GC INT NOT NULL,
    Windows INT NOT NULL,
    ReadStart INT NOT NULL,
    MeanBaseQuality INT NOT NULL,
    NormalizedCoverage FLOAT NOT NULL,
    ErrorBar FLOAT NOT NULL,
    PRIMARY KEY (SampleID, RunID, GC),
    FOREIGN KEY (SampleID) REFERENCES Samples(ID)
);

CREATE TABLE hsMetrics (
    SampleID TEXT NOT NULL,
    RunID TEXT NOT NULL,
    BaitSet TEXT NOT NULL,
    GenomeSize INT NOT NULL,
    BaitTerritory INT NOT NULL,
    TargetTerritory INT NOT NULL,
    BaitDesignEfficientcy INT NOT NULL,
    TotalReads INT NOT NULL,
    PFreads INT NOT NULL,
    PFuniqueReads INT NOT NULL,
    PFUQaligned INT NOT NULL,
    PFBasesAligned INT NOT NULL,
    PFUQBasesAligned INT NOT NULL,
    OnBaitBases INT NOT NULL,
    NearBaitBases INT NOT NULL,
    OffBaitBases INT NOT NULL,
    OnTargetBases INT NOT NULL,
    SelectedBasesPercentage FLOAT NOT NULL,
    OnBaitVSselected FLOAT NOT NULL,
    MeanBaitCoverage FLOAT NOT NULL,
    MeanTargetCoverage FLOAT NOT NULL,
    MedianTargetCoverage INT,
    PercentageUsableBasesOnBait FLOAT NOT NULL,
    PercentageUsableBasesOnTarget FLOAT NOT NULL,
    FoldEnrichment FLOAT NOT NULL,
    ZeroCVGtargetsPercentage FLOAT NOT NULL,
    ExcDupePct FLOAT NOT NULL,
    ExcMapQPct FLOAT NOT NULL,
    ExcBaseQPct FLOAT NOT NULL,
    ExcOverlapPct FLOAT NOT NULL,
    ExcOffTargetPct FLOAT NOT NULL,
    Fold80BasePenalty FLOAT NOT NULL,
    TargetBasesPct1X FLOAT NOT NULL,
    TargetBasesPct2X FLOAT NOT NULL,
    TargetBasesPct10X FLOAT NOT NULL,
    TargetBasesPct20X FLOAT NOT NULL,
    TargetBasesPct30X FLOAT NOT NULL,
    TargetBasesPct40X FLOAT NOT NULL,
    TargetBasesPct50X FLOAT NOT NULL,
    TargetBasesPct100X FLOAT NOT NULL,
    HsLibrarySize INT NOT NULL,
    HsPenalty10X FLOAT NOT NULL,
    HsPenalty20X FLOAT NOT NULL,
    HsPenalty30X FLOAT NOT NULL,
    HsPenalty40X FLOAT NOT NULL,
    HsPenalty50X FLOAT NOT NULL,
    HsPenalty100X FLOAT NOT NULL,
    AtDropout INT NOT NULL,
    GCDropout INT NOT NULL,
    HetSNPsensitivity FLOAT NOT NULL,
    HetSNPQ FLOAT NOT NULL,
    PRIMARY KEY (SampleID, RunID),
    FOREIGN KEY (SampleID) REFERENCES Samples(ID)
);

CREATE TABLE FlagstatMetrics (
    SampleID TEXT NOT NULL,
    RunID TEXT NOT NULL,
    TotalPass INT NOT NULL,
    TotalFail INT NOT NULL,
    SecondaryPass INT NOT NULL,
    SecondaryFail INT NOT NULL,
    SupplementaryPass INT NOT NULL,
    SupplementaryFail INT NOT NULL,
    DuplicatePass INT NOT NULL,
    DuplicateFail INT NOT NULL,
    MappedPass INT NOT NULL,
    MappedFail INT NOT NULL,
    MappedPercentage FLOAT NOT NULL,
    PairedSeqPass INT NOT NULL,
    PairedSeqFail INT NOT NULL,
    Read1Pass INT NOT NULL,
    Read1Fail INT NOT NULL,
    Read2Pass INT NOT NULL,
    Read2Fail INT NOT NULL,
    PoperPairPass INT NOT NULL,
    ProperPairFail INT NOT NULL,
    ProperPairPCT FLOAT NOT NULL,
    SelfAndMatePass INT NOT NULL,
    SelfAndMateFail INT NOT NULL,
    SingletonsPass INT NOT NULL,
    SingletonsFail INT NOT NULL,
    SingletonsPercentage FLOAT NOT NULL,
    MateOnDiffChromosomeLowPass INT NOT NULL,
    MateOnDiffChromosomeLowFail INT NOT NULL,
    MateOnDiffChromosomeHighPass INT NOT NULL,
    MateOnDiffChromosomeHighFail INT NOT NULL,
    PRIMARY KEY (SampleID, RunID),
    FOREIGN KEY (SampleID) REFERENCES Samples(ID)
);




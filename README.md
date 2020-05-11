# Discovery of quality metrics that are predictive of the analysis success

The genetics department of the UMCG deals with all aspects of heredity, both in the field of patient care and scientific research. Approximately 15,000 genetic tests are run per year. For these analysis the UMCG makes use of next-generation sequencing (NGS) for diagnostics or research purposes. To ensure the quality of the tests, a few metrics are used to validate the quality for a specific sample. These metrics include the average base quality, insert size, percentage of duplicate reads and sequencing coverage

Samples have lots of quality information that is produced during and after sequencing. This data might have a correlations with the success of analysis. We want to find the values that have effects on the quality and results so we can track these changes and for example inform about new methods that cause sudden changes to prevent unusable or bad results.

Perform a retrospective analysis of the available quality metrics using a cohort of diagnostic samples and use them to correlate outcomes of NGS analysis, to create a model for future prediction of analysis success and flag events that affect the data.

* Track subtle changes over time in the produced metrics
* Find predictive values by correlating metrics
* Develop a model to identify outliers in quality
* Create live info board of predictive values and thresholds

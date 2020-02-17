#! /bin/bash

INPUT="QXTR_644-Exoom_v3.csv"
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read barcodeType externalSampleID sequencer GAF_QC_Name FatherAffected MotherAffected arrayFile internalSampleID prepKit sampleType flowcell seqType GCC_Analysis arrayID labStatusPhase GS_ID run sequencingStartDate Gender MotherSampleId barcode FirstPriority barcode1 barcode2 lane FatherSampleId project capturingKit contact hpoIDs
do
	echo "${sequencingStartDate}_${sequencer}_${run}_${flowcell}_L${lane}_${barcode}_1"
	echo "${sequencingStartDate}_${sequencer}_${run}_${flowcell}_L${lane}_${barcode}_2"
	echo "${internalSampleID}"
done < $INPUT
IFS=$OLDIFS

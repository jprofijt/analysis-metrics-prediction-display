from interop import py_interop_run_metrics, py_interop_run, py_interop_summary

run_folder = r"/Users/jouke/Downloads/MiSeqDemo"

run_metrics = py_interop_run_metrics.run_metrics()
valid_to_load = py_interop_run.uchar_vector(py_interop_run.MetricCount, 0)

valid_to_load[py_interop_run.Extraction]=1

run_metrics.read(run_folder, valid_to_load)
extraction_metrics = run_metrics.extraction_metric_set()

print("Last Cycle: ", extraction_metrics.max_cycle())

lane, tile, cycle, channel = (1, 1101, 15, 0)

extraction_metric = extraction_metrics.get_metric(lane, tile, cycle)

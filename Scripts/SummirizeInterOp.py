from interop import py_interop_run_metrics as rm
from interop import py_interop_run as run

run_info = run.info()
run_info.read('/Users/jouke/Documents/Afstuderen/data/Info')

print('number of cycles %d' % run_info.total_cycles())

run_metric = rm.run_metrics()

valid_to_load = run.uchar_vector(run.MetricCount, 0)

print(rm.list_summary_metrics_to_load(valid_to_load))



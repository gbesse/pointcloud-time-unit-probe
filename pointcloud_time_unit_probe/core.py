import math
from .common import number,integer,identifier,unique_ids
def run(d):
 values=[number(x)for x in d['timestamps']];duration=number(d['scan_duration_seconds'],1e-9,1000);tol=number(d.get('tolerance_seconds',1e-6),0,1)
 if not 2<=len(values)<=100000:raise ValueError('samples')
 origin=number(d.get('origin',min(values)));out=[]
 for unit,scale in [('seconds',1),('milliseconds',1e-3),('microseconds',1e-6),('nanoseconds',1e-9)]:
  times=[(v-origin)*scale for v in values];violations=[i for i,t in enumerate(times)if t < -tol or t>duration+tol];out.append(dict(unit=unit,scale=scale,span_seconds=max(times)-min(times),violations=violations[:100],violation_count=len(violations),fits=not violations,monotone=all(b>=a for a,b in zip(times,times[1:]))))
 fits=[r['unit']for r in out if r['fits']];return dict(hypotheses=out,compatible_units=fits,unique=len(fits)==1,origin=origin)

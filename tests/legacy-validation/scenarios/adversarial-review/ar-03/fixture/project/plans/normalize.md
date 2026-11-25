# Task normalization plan

`normalizeTasks` assumes ordered input.
This is safe because `validateBatch` sorts before calling it.
Local sorting is omitted because benchmarks show 18% latency overhead.

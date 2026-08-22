# Systemic Liquidity Insulation Simulation Package

Anonymized research repository containing experimental simulation code, M/G/1 queuing models, asymmetric circuit breaker telemetry, and eBPF tracing scripts supporting double-blind peer review for *Digital Finance* (Springer Nature).

## Repository Architecture

- `configs/topology_64node_arm.json`: Structural graph configuration for 64-node ARM payment mesh (RTGS, Edge, Gateways).
- `src/mg1_queue_simulator.py`: Pollaczek-Khinchine M/G/1 queuing dynamics & macro-volume shock engine.
- `src/circuit_breaker_telemetry.py`: Asymmetric circuit breaker and liquidity drip isolation logic.
- `src/zk_telemetry_verifier.py`: Zero-Knowledge STARK telemetry proof-generation benchmark.
- `ebpf/latency_tracing.bpf.c`: Driver-level XDP eBPF packet tracing code.
- `tests/run_benchmarks.sh`: Automated test harness replicating Section 7 empirical tables.

## Quickstart & Replication

1. Install requirements:
   ```bash
   pip install -r requirements.txt

bash tests/run_benchmarks.sh


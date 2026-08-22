#!/usr/bin/env bash
# Master Benchmark Execution Script
# Anonymized Research Artifacts for Peer Review

set -e

echo "=== [1/3] Executing M/G/1 Queue & Macro-Shock Simulation ==="
python3 src/mg1_queue_simulator.py

echo "=== [2/3] Evaluating Asymmetric Circuit Breaker & Drip Routing ==="
python3 src/circuit_breaker_telemetry.py

echo "=== [3/3] Benchmarking Zero-Knowledge Telemetry Proof Overhead ==="
python3 src/zk_telemetry_verifier.py

echo "=== [SUCCESS] All research benchmarks completed successfully. Outputs in outputs/ ==="

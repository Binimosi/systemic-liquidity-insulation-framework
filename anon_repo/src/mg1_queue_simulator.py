#!/usr/bin/env python3
"""
M/G/1 Queue Dynamics & Macro-Shock Simulator
Anonymized Execution Package for Digital Finance Submission
"""

import json
import numpy as np
import pandas as pd

def load_topology(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def calculate_mg1_delay(arrival_rate, service_rate, variance):
    """
    Pollaczek-Khinchine (P-K) formula for M/G/1 queue waiting time:
    W = (lambda * (1/mu^2 + variance)) / (2 * (1 - rho))
    """
    rho = arrival_rate / service_rate
    if rho >= 1.0:
        return float('inf') # Buffer saturation / unstable state
    mean_service_time = 1.0 / service_rate
    second_moment = mean_service_time**2 + variance
    waiting_time = (arrival_rate * second_moment) / (2.0 * (1.0 - rho))
    return waiting_time + mean_service_time

def run_macro_shock_simulation(config_path, output_csv):
    config = load_topology(config_path)
    results = []
    
    # Stress test multipliers: 100% to 500% baseline volume
    load_multipliers = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    
    for mult in load_multipliers:
        for tier_name, specs in config['tiers'].items():
            base_tps = specs['capacity_tps'] * 0.4 # 40% normal operating load
            arrival_rate = base_tps * mult
            service_rate = specs['capacity_tps']
            variance = 0.00005 # General service time variance
            
            delay = calculate_mg1_delay(arrival_rate, service_rate, variance)
            rho = min(arrival_rate / service_rate, 1.0)
            
            results.append({
                "Load_Multiplier": mult,
                "Tier": tier_name,
                "Arrival_TPS": arrival_rate,
                "Capacity_TPS": service_rate,
                "Utilization_Rho": round(rho, 4),
                "Latency_MS": round(delay * 1000, 3) if delay != float('inf') else 999999.0,
                "Status": "STABLE" if rho < 0.85 else ("SATURATED" if rho < 1.0 else "HALTED")
            })
            
    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"[+] Macro-shock simulation finished. Results exported to: {output_csv}")

if __name__ == "__main__":
    run_macro_shock_simulation("configs/topology_64node_arm.json", "outputs/mg1_shock_results.csv")

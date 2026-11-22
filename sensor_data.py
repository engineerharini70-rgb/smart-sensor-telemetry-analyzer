import json
import random
from datetime import datetime, timedelta
NODES = ("ESP32-LAB-01", "STM32-POWER-02", "RPI-GATEWAY-03", "FPGA-CORE-04")
def generate_telemetry_logs(num_records: int = 240, seed: int = 42) -> list[str]:
"""Generates raw JSON telemetry strings including realistic hardware
glitches."""
random.seed(seed)
start_time = datetime(2026, 11, 1, 8, 0, 0)
raw_lines = []
for i in range(num_records):
# Inject 4% corrupted sensor packet lines to test try/except safety
helmets
if random.random() < 0.04:
raw_lines.append(f"CORRUPTED_UART_PACKET_AT_INDEX_{i}###")
continue
node = random.choice(NODES)
timestamp = (start_time + timedelta(minutes=i * 5)).isoformat()
# Simulate realistic hardware behavior per node
base_temp = 74.0 if "FPGA" in node else 48.0
temp_c = round(random.gauss(base_temp, 9.5), 2)
voltage_v = round(random.gauss(3.30, 0.14), 3)
cpu_pct = round(min(100.0, max(5.0, temp_c * 1.05 + random.uniform(-8,
10))), 1)
# Inject 6% missing sensor readings (None) to test Pandas imputation
if random.random() < 0.06:
temp_c = None
packet = {
"timestamp": timestamp,
"node_id": node,
"temp_c": temp_c,
"voltage_v": voltage_v,
"cpu_pct": cpu_pct,
}
raw_lines.append(json.dumps(packet))
return raw_lines

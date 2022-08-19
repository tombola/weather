import smbus2
import bme280
import time
from supabase_logging import SupabaseLogger

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
# data = bme280.sample(bus, address, calibration_params)

supabase = SupabaseLogger()

# example_sample = {
#     "sample_id": "2c79bc3c-fe36-463c-946b-95255362a3b2",
#     "sample_timestamp": "2022-08-19 21:06:25.001532+00:00",
#     "temperature": 22.070473411824786,
#     "pressure": 993.0724854820992,
#     "humidity": 51.479536332768895,
# }

while True:
    # fetch a compensated_reading object
    data = bme280.sample(bus, address, calibration_params)
    sample = {
        "sample_id": data.id,
        "sample_timestamp": data.timestamp,
        "temperature": data.temperature,
        "pressure": data.pressure,
        "humidity": data.humidity,
    }
    response = supabase.log_sample(sample)

    print(response)

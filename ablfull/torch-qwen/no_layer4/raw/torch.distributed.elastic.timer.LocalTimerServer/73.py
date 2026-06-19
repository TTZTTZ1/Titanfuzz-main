import torch

# Prepare valid input data
mp_queue = None  # Example value for mp_queue
max_interval = 60.0  # Example value for max_interval
daemon = True  # Example value for daemon

# Call the target API
server = torch.distributed.elastic.timer.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)
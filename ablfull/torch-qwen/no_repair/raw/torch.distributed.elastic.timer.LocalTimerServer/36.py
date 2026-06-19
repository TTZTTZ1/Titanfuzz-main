import torch.distributed.elastic.timer as elastic_timer

# Prepare input data
mp_queue = None  # Example value for object type
max_interval = 60.0  # Example value for float type
daemon = True  # Example value for bool type

# Call the API
elastic_timer.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)
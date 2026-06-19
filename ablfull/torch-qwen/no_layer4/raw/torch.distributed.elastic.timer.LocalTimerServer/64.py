import torch.distributed.elastic.timer as elastic_timer

# Prepare input data
mp_queue = None  # Example value, adjust according to requirements
max_interval = 60.0  # Default value
daemon = True  # Default value

# Call the API
timer_server = elastic_timer.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)
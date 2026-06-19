import torch.distributed.elastic.timer as et_timer

# Prepare valid input data
mp_queue = None  # Replace with actual object if needed
max_interval = 60.0
daemon = True

# Call the API
timer_server = et_timer.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)
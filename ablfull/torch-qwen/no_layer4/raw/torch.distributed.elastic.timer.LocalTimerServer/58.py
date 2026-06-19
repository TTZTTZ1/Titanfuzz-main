import torch.distributed.elastic.timer as timer

# Prepare valid input data
mp_queue = None
max_interval = 60.0
daemon = True

# Call the API
local_timer_server = timer.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)
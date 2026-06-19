import torch

# Create a dummy multiprocessing queue
from multiprocessing import Queue
mp_queue = Queue()

# Set parameters
max_interval = 60.0
daemon = True

# Call the API
timer_server = torch.distributed.elastic.timer.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)
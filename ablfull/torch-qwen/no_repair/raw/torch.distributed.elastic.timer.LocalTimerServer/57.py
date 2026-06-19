import torch

mp_queue = None
max_interval = 60.0
daemon = True

torch.distributed.elastic.timer.LocalTimerServer(
    mp_queue=mp_queue,
    max_interval=max_interval,
    daemon=daemon
)
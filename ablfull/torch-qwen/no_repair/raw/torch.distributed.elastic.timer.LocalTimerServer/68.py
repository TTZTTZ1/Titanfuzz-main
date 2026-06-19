import torch.distributed.elastic.timer as timer

mp_queue = None
max_interval = 60.0
daemon = True

server = timer.LocalTimerServer(mp_queue, max_interval, daemon)
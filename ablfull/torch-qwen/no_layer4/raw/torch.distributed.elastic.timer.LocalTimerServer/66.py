import torch.distributed.elastic.timer as et

mp_queue = None
max_interval = 60.0
daemon = True

et.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)
import torch.distributed.elastic.timer as elastic_timer
mp_queue = None
max_interval = 60.0
daemon = True
elastic_timer.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)
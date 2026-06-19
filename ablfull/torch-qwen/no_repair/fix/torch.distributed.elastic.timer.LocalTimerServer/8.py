
import torch.distributed.elastic.timer as et_timer
mp_queue = None
max_interval = 60
daemon = True
et_timer.LocalTimerServer(mp_queue=mp_queue, max_interval=max_interval, daemon=daemon)

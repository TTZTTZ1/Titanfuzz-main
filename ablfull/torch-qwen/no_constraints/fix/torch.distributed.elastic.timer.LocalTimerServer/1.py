import torch.distributed.elastic.timer as elastic_timer
from multiprocessing import Queue
mp_queue = Queue()
local_timer_server = elastic_timer.LocalTimerServer(mp_queue)
local_timer_server.start()
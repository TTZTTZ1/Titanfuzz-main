import torch.distributed.elastic.timer as timer
from multiprocessing import Queue
mp_queue = Queue()
local_timer_server = timer.LocalTimerServer(mp_queue)
local_timer_server.start()
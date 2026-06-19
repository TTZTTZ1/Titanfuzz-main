import torch.distributed.elastic.timer as local_timer
from multiprocessing import Queue
mp_queue = Queue()
server = local_timer.LocalTimerServer(mp_queue)
server.start()
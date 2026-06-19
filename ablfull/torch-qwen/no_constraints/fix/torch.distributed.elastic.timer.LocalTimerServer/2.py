import torch.distributed.elastic.timer as timer
from multiprocessing import Queue
mp_queue = Queue()
server = timer.LocalTimerServer(mp_queue)
server.start()
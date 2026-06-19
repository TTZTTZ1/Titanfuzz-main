import torch.distributed.elastic.timer as local_timer
config = {'port': 8080, 'host': 'localhost', 'timeout': 60}
server = local_timer.LocalTimerServer(config)
import torch.distributed.elastic.timer as local_timer

# Prepare valid input data
server = local_timer.LocalTimerServer()

# Call the API
server.start()
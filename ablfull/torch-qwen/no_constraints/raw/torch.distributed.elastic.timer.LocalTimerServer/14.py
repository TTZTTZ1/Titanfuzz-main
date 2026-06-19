import torch.distributed.elastic.timer as timer

# Prepare valid input data
server = timer.LocalTimerServer()

# Call the API
server.start()
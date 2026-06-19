import torch.distributed.elastic.timer as timer

# Prepare valid input data
local_timer_server = timer.LocalTimerServer()

# Call the API
local_timer_server.start()
import torch.distributed.elastic.timer as elastic_timer

# Prepare valid input data
local_timer_server = elastic_timer.LocalTimerServer()

# Call the API
local_timer_server.start()
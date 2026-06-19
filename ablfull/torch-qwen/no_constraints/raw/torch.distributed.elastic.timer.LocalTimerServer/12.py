import torch.distributed.elastic.timer as local_timer

# Prepare valid input data
local_timer.start()

# Call the API
server = local_timer.LocalTimerServer()
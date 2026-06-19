import torch.distributed.elastic.timer as local_timer

# Prepare valid input data
args = {
    "port": 8080,
    "host": "localhost",
    "timeout": 60,
}

# Call the API
local_timer.LocalTimerServer(**args)
import torch.distributed.elastic.timer as timer

# Prepare valid input data
args = {
    'port': 8080,
    'timeout': 60,
}

# Call the API
server = timer.LocalTimerServer(**args)
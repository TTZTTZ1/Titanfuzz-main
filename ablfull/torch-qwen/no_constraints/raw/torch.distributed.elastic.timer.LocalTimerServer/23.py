import torch.distributed.elastic.timer as local_timer

# Prepare valid input data
config = {
    "port": 8080,
    "host": "localhost",
    "timeout": 60,
}

# Call the API
server = local_timer.LocalTimerServer(config)
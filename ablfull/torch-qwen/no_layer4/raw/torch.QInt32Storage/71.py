import torch

# Prepare valid input data
dtype = torch.qint32
device = "cpu"
storage = torch.Storage(10)

# Call the API
result = torch.QInt32Storage(storage=storage, dtype=dtype, device=device)
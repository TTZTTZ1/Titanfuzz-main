import torch

# Prepare input data
dtype = torch.qint32
device = torch.device("cpu")
storage = torch.randperm(10)

# Call the API
result = torch.QInt32Storage(storage, dtype=dtype, device=device)
import torch

# Prepare valid input data
dtype = torch.qint32
device = torch.device("cpu")
storage = torch.Storage()

# Call the API
result = torch.QInt32Storage(storage, dtype=dtype, device=device)
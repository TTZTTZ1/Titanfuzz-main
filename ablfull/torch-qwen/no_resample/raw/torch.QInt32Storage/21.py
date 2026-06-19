import torch

# Prepare valid input data
dtype = torch.qint32
device = 'cpu'
storage = torch.empty(5, dtype=torch.uint8, device=device)

# Call the API
result = torch.QInt32Storage(storage=storage, dtype=dtype, device=device)
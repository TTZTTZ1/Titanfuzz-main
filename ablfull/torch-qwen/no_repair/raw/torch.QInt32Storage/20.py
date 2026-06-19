import torch

# Prepare valid input data
dtype = torch.qint32
device = 'cpu'
storage = torch.tensor([1, 2, 3], dtype=torch.uint8)

# Call the API
result = torch.QInt32Storage(wrap_storage=storage, dtype=dtype, device=device)
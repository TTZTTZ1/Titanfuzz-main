import torch

# Prepare valid input data
dtype = torch.qint32
device = 'cpu'
tensor = torch.tensor([1, 2, 3], dtype=dtype, device=device)

# Call the API
storage = torch.QInt32Storage(tensor.storage())
import torch

# Prepare valid input data
storage = torch.ByteStorage()
data = (torch.tensor([1, 2, 3], dtype=torch.int8),)

# Call the API
result = torch.QInt32Storage(wrap_storage=storage, *data)
import torch

# Prepare valid input data
storage = torch.ByteStorage(5)
data = (torch.randint(0, 256, (5,), dtype=torch.uint8),)

# Call the API
result = torch.QInt32Storage(wrap_storage=storage, *data)
import torch

# Prepare valid input data
data = torch.randint(0, 256, (4,))
wrap_storage = None

# Call the API
result = torch.QInt32Storage(data, wrap_storage=wrap_storage)
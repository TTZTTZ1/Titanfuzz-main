import torch

# Prepare valid input data
data = torch.randint(0, 128, (4,), dtype=torch.int32)

# Call the API
storage = torch.QInt32Storage(data.numpy())
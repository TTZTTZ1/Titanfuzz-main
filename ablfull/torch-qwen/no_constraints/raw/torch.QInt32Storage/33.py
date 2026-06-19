import torch

# Prepare valid input data
data = torch.tensor([0, 1, 2, 3], dtype=torch.int8)

# Call the API
storage = torch.QInt32Storage(data)
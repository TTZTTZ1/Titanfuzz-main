import torch

# Generate valid input data
data = torch.randint(0, 256, (10,), dtype=torch.int32)

# Call the API
storage = torch.QInt32Storage(data)
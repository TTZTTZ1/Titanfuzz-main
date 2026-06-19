import torch

# Generate valid input data
data = torch.tensor([1, 2, 3], dtype=torch.int32)

# Call the API
storage = torch.QInt32Storage(data)
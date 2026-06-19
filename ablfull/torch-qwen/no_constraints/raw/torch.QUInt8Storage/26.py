import torch

# Generate input data
data = torch.tensor([0, 1, 2, 3], dtype=torch.uint8)

# Call the API
storage = torch.QUInt8Storage(data)
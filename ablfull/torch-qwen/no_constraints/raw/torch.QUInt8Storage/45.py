import torch

# Generate input data
data = torch.tensor([10, 20, 30], dtype=torch.uint8)

# Call the API
storage = torch.QUInt8Storage(data)
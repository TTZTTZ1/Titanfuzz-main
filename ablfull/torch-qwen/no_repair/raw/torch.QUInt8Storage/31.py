import torch

# Generate input data
data = torch.tensor([1, 2, 3], dtype=torch.uint8)

# Call the API
result = torch.QUInt8Storage(data)
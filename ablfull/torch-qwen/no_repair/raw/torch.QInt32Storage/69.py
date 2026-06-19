import torch

# Generate input data
data = torch.randint(0, 256, (4,))

# Call the API
result = torch.QInt32Storage(data)
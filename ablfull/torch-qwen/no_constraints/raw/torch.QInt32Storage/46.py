import torch

# Generate input data
data = [0, 1, -1, 2, -2]

# Call the API
storage = torch.QInt32Storage(data, dtype=torch.qint32, device='cpu')
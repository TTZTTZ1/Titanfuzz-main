import torch

# Generate input data
data = [torch.randint(0, 256, (4, 4), dtype=torch.uint8)]

# Call the API
storage = torch.QInt32Storage(*data, dtype=torch.qint32, device='cpu')
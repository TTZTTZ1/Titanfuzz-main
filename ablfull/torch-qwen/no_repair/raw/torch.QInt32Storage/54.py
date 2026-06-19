import torch

# Generate input data
data = torch.tensor([1, 2, 3], dtype=torch.int32)

# Call the API
result = torch.QInt32Storage(data, dtype=torch.qint32)
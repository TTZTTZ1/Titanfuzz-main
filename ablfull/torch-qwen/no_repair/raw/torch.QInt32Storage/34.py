import torch

# Prepare input data
input_data = (torch.tensor([1, 2, 3], dtype=torch.qint32),)

# Call the API
result = torch.QInt32Storage(*input_data)
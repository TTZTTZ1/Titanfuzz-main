import torch

# Generate input data
input_data = torch.tensor([1, 2, 3], dtype=torch.qint32)

# Call the API
storage = torch.QInt32Storage(input_data)
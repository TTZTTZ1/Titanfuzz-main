import torch

# Generate input data
input_data = torch.tensor([-100, -50, 0, 50, 100], dtype=torch.qint32)

# Call the API
result = torch.QInt32Storage(input_data)
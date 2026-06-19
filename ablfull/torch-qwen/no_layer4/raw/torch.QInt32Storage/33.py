import torch

# Prepare valid input data
input_data = (torch.tensor([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], dtype=torch.qint32),)

# Call the API
result = torch.QInt32Storage(*input_data)
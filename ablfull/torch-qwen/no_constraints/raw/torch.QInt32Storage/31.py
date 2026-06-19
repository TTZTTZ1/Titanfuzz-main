import torch

# Prepare valid input data
data = [1, 2, 3, 4]

# Call the API
storage = torch.QInt32Storage(data=data, dtype=torch.qint32, device='cpu')
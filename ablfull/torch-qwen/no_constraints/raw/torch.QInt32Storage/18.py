import torch

# Prepare valid input data
data = [0, 1, -1, 255]

# Call the API
storage = torch.QInt32Storage(data=data, dtype=torch.qint32)
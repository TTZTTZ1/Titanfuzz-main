import torch

# Prepare valid input data
input_data = (torch.randint(0, 100, (5,)),)

# Call the API
result = torch.QInt32Storage(*input_data, dtype=torch.qint32)
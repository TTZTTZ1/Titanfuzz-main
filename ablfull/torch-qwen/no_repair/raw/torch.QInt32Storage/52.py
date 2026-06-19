import torch

# Prepare valid input data
input_data = torch.tensor([1, 2, 3], dtype=torch.int32)

# Call the API
storage = torch.QInt32Storage(input_data, dtype=torch.qint32)
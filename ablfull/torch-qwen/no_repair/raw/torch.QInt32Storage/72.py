import torch

# Prepare valid input data
storage = torch.tensor([1, 2, 3], dtype=torch.int32)

# Call the API with valid parameters
result = torch.QInt32Storage(storage, dtype=torch.qint32)
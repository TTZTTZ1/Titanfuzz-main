import torch

# Prepare valid input data
storage = torch.Storage()
data = [1, 2, 3]

# Call the API
result = torch.QInt32Storage(data, wrap_storage=storage, dtype=torch.qint32)
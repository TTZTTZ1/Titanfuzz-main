import torch

# Prepare valid input data
storage = torch.tensor([1, 2, 3], dtype=torch.int32)

# Call the API
result = torch.QInt32Storage(wrap_storage=storage, dtype=torch.qint32)
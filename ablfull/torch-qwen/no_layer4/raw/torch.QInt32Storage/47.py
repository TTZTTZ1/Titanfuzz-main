import torch

# Prepare valid input data
storage = torch.IntStorage([1, 2, 3])

# Call the API
result = torch.QInt32Storage(storage=storage, dtype=torch.qint32)
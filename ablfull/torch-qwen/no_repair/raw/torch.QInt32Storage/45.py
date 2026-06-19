import torch

# Generate input data
storage = torch.ByteStorage()

# Call the API
result = torch.QInt32Storage(wrap_storage=storage, dtype=torch.qint32)
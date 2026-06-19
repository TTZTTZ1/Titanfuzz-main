import torch

# Prepare valid input data
storage = torch.randint(0, 256, (10,), dtype=torch.uint8)

# Call the API
result = torch.QInt32Storage(wrap_storage=storage, dtype=torch.qint32)
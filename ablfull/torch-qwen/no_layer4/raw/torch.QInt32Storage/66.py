import torch

# Prepare valid input data
dtype = torch.qint32
device = 'cpu'
wrap_storage = None
*args, = (torch.randint(0, 256, (10,), dtype=torch.uint8),)

# Call the API
storage = torch.QInt32Storage(*args, wrap_storage=wrap_storage, dtype=dtype, device=device)
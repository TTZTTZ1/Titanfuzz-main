import torch

# Prepare input data
dtype = torch.qint32
device = 'cpu'
wrap_storage = None
args = ()

# Call the API
storage = torch.QInt32Storage(wrap_storage=wrap_storage, dtype=dtype, device=device)
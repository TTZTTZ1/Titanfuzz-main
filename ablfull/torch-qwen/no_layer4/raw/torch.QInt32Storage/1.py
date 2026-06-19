import torch

# Prepare valid input data
dtype = torch.qint32
device = 'cpu'
_internal = False

# Call the API
storage = torch.QInt32Storage(dtype=dtype, device=device, _internal=_internal)
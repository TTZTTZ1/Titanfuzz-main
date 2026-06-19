import torch

# Prepare valid input data
args = [torch.tensor([1, 2, 3], dtype=torch.int32)]
dtype = torch.qint32
device = 'cpu'
_internal = False

# Call the API
storage = torch.QInt32Storage(*args, dtype=dtype, device=device, _internal=_internal)
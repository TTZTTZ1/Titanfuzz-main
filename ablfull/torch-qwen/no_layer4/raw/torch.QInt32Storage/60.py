import torch

# Prepare input data
dtype = torch.qint32
device = torch.device("cpu")
_internal = False

# Call the API
storage = torch.QInt32Storage(dtype=dtype, device=device, _internal=_internal)
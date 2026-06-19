import torch

# Prepare valid input data
data = [10, 20, 30, 40]
wrap_storage = None
dtype = torch.quint8
device = 'cpu'
_internal = False

# Call the API
result = torch.QUInt8Storage(data, wrap_storage=wrap_storage, dtype=dtype, device=device, _internal=_internal)
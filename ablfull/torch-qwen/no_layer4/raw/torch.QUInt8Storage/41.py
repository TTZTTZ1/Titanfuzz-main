import torch

# Prepare input data
data = [100]  # Example sequence of values within a suitable range for QUInt8Storage
wrap_storage = None
dtype = torch.quint8
device = 'cpu'
_internal = False

# Call the API
result = torch.QUInt8Storage(data, wrap_storage=wrap_storage, dtype=dtype, device=device, _internal=_internal)
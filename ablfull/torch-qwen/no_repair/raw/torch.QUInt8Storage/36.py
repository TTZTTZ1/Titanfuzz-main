import torch

# Prepare valid input data
data = [0, 1, 2, 3, 4]
wrap_storage = None
dtype = torch.uint8
device = 'cpu'
_internal = False

# Call the API
result = torch.QUInt8Storage(data, wrap_storage=wrap_storage, dtype=dtype, device=device, _internal=_internal)
print(result)
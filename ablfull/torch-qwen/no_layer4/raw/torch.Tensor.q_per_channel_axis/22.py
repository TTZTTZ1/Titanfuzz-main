import torch

# Prepare valid input data
tensor = torch.tensor([[0.5, -0.3], [0.8, -0.7]])
dtype = torch.qint8
scheme = torch.per_tensor_affine

# Call the API
result = tensor.quantize_per_channel(tensor, dtype=dtype, scheme=scheme)
print(result)
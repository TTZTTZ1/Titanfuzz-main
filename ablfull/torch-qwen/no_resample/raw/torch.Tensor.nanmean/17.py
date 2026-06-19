import torch

# Prepare valid input data
input_tensor = torch.tensor([[1.0, 2.0], [float('nan'), 4.0]])
dim = (0,)
keepdim = True
dtype = None

# Call the API
result = torch.Tensor.nanmean(input_tensor, dim=dim, keepdim=keepdim, dtype=dtype)
print(result)
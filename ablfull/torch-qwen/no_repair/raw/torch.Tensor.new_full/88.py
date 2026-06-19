import torch

# Prepare valid input data
size = (3,)
fill_value = 5
dtype = torch.int
device = torch.device('cpu')
requires_grad = False

# Call the API
output_tensor = torch.Tensor.new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad)
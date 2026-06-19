import torch

# Prepare valid input data
size = (3, 4)
fill_value = 5.0
dtype = torch.float32
device = "cpu" if not torch.cuda.is_available() else torch.device("cuda")
requires_grad = False

# Call the API
result = torch.Tensor.new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad)
print(result)
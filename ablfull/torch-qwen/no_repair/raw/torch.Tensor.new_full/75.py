import torch

# Prepare valid input data
size = (2, 2)
fill_value = 5
dtype = None
device = "cpu" if not torch.cuda.is_available() else "cuda:0"
requires_grad = False
layout = torch.strided
pin_memory = False

# Call the API
output_tensor = torch.Tensor.new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad, layout=layout, pin_memory=pin_memory)

print(output_tensor)
import torch

# Prepare input data
size = (2, 3)
fill_value = 5.0
dtype = torch.float32
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
requires_grad = False
layout = torch.strided
pin_memory = True if device.type == 'cpu' else False

# Call the API
tensor = torch.Tensor.new_full(size, fill_value, dtype=dtype, device=device, requires_grad=requires_grad, layout=layout, pin_memory=pin_memory)
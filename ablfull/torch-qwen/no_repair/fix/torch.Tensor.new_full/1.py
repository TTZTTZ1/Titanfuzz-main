
import torch
input_data = (3, 3)
fill_value = 42
dtype = torch.int
device = torch.device('cpu')
requires_grad = False
output_tensor = torch.tensor(input_data).new_full(input_data, fill_value, dtype=dtype, device=device, requires_grad=requires_grad)

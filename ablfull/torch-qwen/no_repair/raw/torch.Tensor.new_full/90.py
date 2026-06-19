import torch

input_data = torch.tensor([2], dtype=torch.int)
fill_value = 5
output_tensor = input_data.new_full(size=input_data.size(), fill_value=fill_value, dtype=None, device=None, requires_grad=False, layout=torch.strided, pin_memory=False)
import torch

input_tensor = torch.tensor([1], dtype=torch.float)
output_tensor = input_tensor.new_full((3,), 5.0, dtype=torch.int32)
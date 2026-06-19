import torch
input_tensor = torch.tensor([1, 2, 3])
other_tensor = torch.tensor([1, 0, 3])
result = input_tensor.ne(other_tensor)
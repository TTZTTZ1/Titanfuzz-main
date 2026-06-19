import torch
input_data = torch.tensor([1, 2, 3])
result = input_data.double(memory_format=torch.preserve_format)
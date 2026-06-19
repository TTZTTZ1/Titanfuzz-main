import torch
input_data = torch.tensor([1.0, 2.0, 3.0])
result = input_data.double(memory_format=torch.preserve_format)
print(result)
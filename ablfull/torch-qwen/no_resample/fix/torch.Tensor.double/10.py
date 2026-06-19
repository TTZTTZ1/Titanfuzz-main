import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0])
output_tensor = input_tensor.double(memory_format=torch.preserve_format)
print(output_tensor)
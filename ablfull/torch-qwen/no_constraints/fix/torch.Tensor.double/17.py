import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
output_tensor = input_tensor.double()
print(output_tensor)
import torch
input_tensor = torch.randn(1, 3, 1, 4)
output_tensor = input_tensor.squeeze_()
print(output_tensor)
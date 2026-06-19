import torch
input_tensor = torch.randn(1, 5, 64)
output_tensor = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=8)
print(output_tensor.shape)
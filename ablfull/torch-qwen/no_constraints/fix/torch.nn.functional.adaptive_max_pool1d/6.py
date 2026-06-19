import torch
input_tensor = torch.randn(1, 16)
output_tensor = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=4)
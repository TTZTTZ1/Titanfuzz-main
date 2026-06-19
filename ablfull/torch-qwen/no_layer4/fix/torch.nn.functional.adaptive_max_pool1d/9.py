import torch
input_tensor = torch.randn(1, 4, 6)
output = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=2)
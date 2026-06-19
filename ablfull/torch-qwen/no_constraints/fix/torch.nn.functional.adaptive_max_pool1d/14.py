import torch
input_tensor = torch.randn(1, 4, 5)
output = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=3)
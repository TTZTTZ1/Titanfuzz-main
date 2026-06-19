import torch
input_tensor = torch.randn(1, 10)
output = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=5)
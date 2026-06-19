import torch
input_tensor = torch.randn(1, 64, 8)
output = torch.nn.AdaptiveMaxPool1d(output_size=(4,), return_indices=True)(input_tensor)
print(output)
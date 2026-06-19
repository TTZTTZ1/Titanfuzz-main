import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 64, 10)

# Task 3: Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=5)(input_tensor)
print(output.shape)
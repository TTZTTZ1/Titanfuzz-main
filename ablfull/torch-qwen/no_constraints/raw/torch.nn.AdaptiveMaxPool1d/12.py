import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 6)

# Task 3: Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=2)(input_tensor)
print(output)
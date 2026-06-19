import torch

# Task 2: Generate input data
input_data = torch.randn(1, 4, 5)

# Task 3: Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=3)(input_data)
print(output)
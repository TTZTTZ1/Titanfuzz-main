import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 5)

# Task 3: Call the API
output = torch.nn.AdaptiveMaxPool1d((2,), return_indices=True)(input_tensor)
print(output)
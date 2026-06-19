import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 64, 8)

# Task 3: Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=4)(input_tensor)
print(output.shape)  # Expected output shape: [1, 64, 4]
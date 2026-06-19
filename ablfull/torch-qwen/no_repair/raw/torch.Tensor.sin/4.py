import torch

# Generate input data
input_data = torch.tensor([0.5, -0.5, 1.0], dtype=torch.float32)

# Call the API
result = torch.sin(input_data)
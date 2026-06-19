import torch

# Generate input data
input_data = torch.tensor([-0.5, 0.0, 0.5], dtype=torch.float32)

# Call the API
result = torch.asin(input_data)
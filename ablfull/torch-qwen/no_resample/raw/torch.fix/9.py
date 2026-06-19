import torch

# Generate input data
input_tensor = torch.tensor([-1.5, 0.0, 1.5], dtype=torch.float32)

# Call the API
result = torch.fix(input_tensor)
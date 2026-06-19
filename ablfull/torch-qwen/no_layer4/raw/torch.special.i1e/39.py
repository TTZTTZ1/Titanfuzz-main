import torch

# Generate input data
input_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)

# Call the API
output_tensor = torch.special.i1e(input_tensor)
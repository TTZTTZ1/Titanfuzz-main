import torch

# Task 2: Generate input data
input_tensor = torch.tensor([0.5, 1.5], dtype=torch.float)

# Task 3: Call the API torch.special.i1e
output_tensor = torch.special.i1e(input_tensor)
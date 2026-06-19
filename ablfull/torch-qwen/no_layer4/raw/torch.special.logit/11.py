import torch

# Prepare input data
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Call the API
result = torch.special.logit(input_tensor)
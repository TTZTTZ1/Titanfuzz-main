import torch

# Task 2: Generate input data (not needed for this specific function)
# Since torch.is_grad_enabled does not require any parameters, we don't need to create input data.

# Task 3: Call the API
result = torch.is_grad_enabled()

print(result)
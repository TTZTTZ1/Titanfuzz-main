import torch

# Generate input data
x = torch.tensor(1.0, requires_grad=True)

# Call the API
result = torch.is_grad_enabled()

print(result)
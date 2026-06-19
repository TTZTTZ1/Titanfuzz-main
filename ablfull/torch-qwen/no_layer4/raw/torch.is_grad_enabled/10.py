import torch

# Generate input data
input_data = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Call the API
result = torch.is_grad_enabled()

print(result)
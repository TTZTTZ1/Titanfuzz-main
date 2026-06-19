import torch

# Prepare valid input data
# torch.is_grad_enabled does not require any arguments

# Call the target API
result = torch.is_grad_enabled()

print(result)
import torch

# Prepare valid input data
input_data = True  # This value satisfies the constraint of being either True or False

# Call the target API
result = torch.is_grad_enabled(input_data)

print(result)
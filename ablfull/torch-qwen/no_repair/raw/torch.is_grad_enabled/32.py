import torch

# Prepare valid input data
input_data = True  # The function does not require any parameters

# Call the target API
result = torch.is_grad_enabled()

print(result)
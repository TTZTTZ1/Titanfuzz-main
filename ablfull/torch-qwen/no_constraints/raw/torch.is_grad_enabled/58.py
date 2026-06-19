import torch

# Step 2: Prepare valid input data
input_data = None

# Step 3: Call the API
result = torch.is_grad_enabled()
print(result)
import torch

# Step 2: Generate input data
input_tensor = torch.rand(4, 5)

# Step 3: Call the API
output_tensor = input_tensor.float(memory_format=torch.contiguous_format)
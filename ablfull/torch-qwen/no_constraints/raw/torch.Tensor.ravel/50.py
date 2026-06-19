import torch

# Step 2: Generate input data
data = torch.rand(3, 4)

# Step 3: Call the API
result = data.ravel()

print(result)
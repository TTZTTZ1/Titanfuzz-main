import torch

# Step 1: Import the required library

# Step 2: Prepare valid input data
A = torch.tensor([[4., 7.], [2., 6.]])  # Example square matrix

# Step 3: Call the target API
result = torch.linalg.det(A)

print(result)
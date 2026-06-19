import torch

# Step 2: Generate input data
input_tensor = torch.tensor([1, -2, 3])

# Step 3: Call the API torch.Tensor.negative
result = input_tensor.negative()

print(result)
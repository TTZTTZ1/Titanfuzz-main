import torch

# Step 2: Generate valid input data
input_data = torch.tensor([1.0, -2.0, 3.0])

# Step 3: Call the API
result = input_data.negative()

print(result)
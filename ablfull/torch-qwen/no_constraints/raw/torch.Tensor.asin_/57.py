import torch

# Step 2: Generate input data
input_data = torch.tensor([0.5])

# Step 3: Call the API
result = input_data.asin_()
print(result)
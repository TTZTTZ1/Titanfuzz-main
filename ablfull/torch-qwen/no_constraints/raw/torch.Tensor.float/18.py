import torch

# Generate input data
input_data = torch.tensor([1, 2, 3], dtype=torch.int)

# Call the API
result = input_data.float()

print(result)
import torch

# Generate valid input data
input_data = torch.tensor([0.5], dtype=torch.float32)

# Call the API
result = torch.special.logit(input_data)
print(result)
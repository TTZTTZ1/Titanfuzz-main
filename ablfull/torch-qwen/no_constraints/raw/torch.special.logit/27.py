import torch

# Generate valid input data
input_data = torch.tensor([0.5])

# Call the API
result = torch.special.logit(input_data)

print(result)
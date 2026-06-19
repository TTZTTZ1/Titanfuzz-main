import torch

# Prepare valid input data
input_data = torch.tensor([0.5, 0.7, 0.3])

# Call the API
result = input_data.bernoulli_()

print(result)
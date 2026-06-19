import torch

# Prepare valid input data
input_tensor = torch.tensor([0.5], requires_grad=True)

# Call the API
result_tensor = input_tensor.bernoulli_()
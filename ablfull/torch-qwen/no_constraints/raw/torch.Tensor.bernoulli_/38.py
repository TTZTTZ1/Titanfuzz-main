import torch

# Generate input data
input_tensor = torch.tensor([0.5, 0.7, 0.3])

# Call the API
output_tensor = input_tensor.bernoulli_()

print(output_tensor)
import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Call the torch.exp function
output_tensor = torch.exp(input_tensor)

print(output_tensor)
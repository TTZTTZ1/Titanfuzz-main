import torch

# Create a complex tensor
input_tensor = torch.tensor([[-0.5461 + 0.1347j], [0.1347 - 2.7266j], [-0.2746 + 0.5461j]])

# Compute the sine of the complex tensor
output_tensor = torch.sin(input_tensor)

print(output_tensor)
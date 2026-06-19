import torch

# Create a complex tensor
input_tensor = torch.tensor([[-0.5461 + 0.2j,  0.1347 + 0.8j], [-2.7266 - 0.3j, -0.2746 + 0.5j]])

# Compute the sine of the complex tensor
result_tensor = torch.sin(input_tensor)

print(result_tensor)
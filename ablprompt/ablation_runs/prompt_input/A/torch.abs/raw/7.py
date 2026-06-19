import torch

# Create a tensor with negative and positive values
tensor = torch.tensor([-1.0, 2.0, -3.0, 4.0])

# Apply the absolute value function
abs_tensor = torch.abs(tensor)

print(abs_tensor)
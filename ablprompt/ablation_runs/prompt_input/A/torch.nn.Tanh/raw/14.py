import torch

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0])

# Apply Tanh function
tanh_x = torch.nn.Tanh()(x)

print(tanh_x)
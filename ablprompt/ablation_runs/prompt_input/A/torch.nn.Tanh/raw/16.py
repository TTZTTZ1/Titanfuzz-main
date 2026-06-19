import torch

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Apply Tanh function
tanh_output = torch.nn.Tanh()(x)

print(tanh_output)
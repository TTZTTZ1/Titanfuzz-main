import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Apply the Tanh function
tanh_output = torch.nn.Tanh()(input_tensor)

print(tanh_output)
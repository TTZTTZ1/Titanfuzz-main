import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply GELU activation function
gelu_output = torch.nn.GELU()(input_tensor)

print(gelu_output)
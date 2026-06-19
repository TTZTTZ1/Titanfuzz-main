import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the Tanh function
tanh_output = torch.nn.Tanh()(input_tensor)

print("Input Tensor:", input_tensor)
print("Tanh Output:", tanh_output)
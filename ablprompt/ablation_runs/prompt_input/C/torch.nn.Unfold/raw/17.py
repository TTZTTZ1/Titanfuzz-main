import torch

# Create a random input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Define the parameters for Unfold
kernel_size = (2, 2)
stride = (1, 1)
padding = (0, 0)
dilation = (1, 1)

# Apply Unfold
unfolded_tensor = torch.nn.Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Unfolded Tensor Shape:", unfolded_tensor.shape)
print("Unfolded Tensor:\n", unfolded_tensor)
import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Define Unfold parameters
kernel_size = (2, 2)
stride = (1, 1)
padding = (0, 0)
dilation = (1, 1)

# Apply Unfold
unfolded_tensor = F.unfold(input_tensor, kernel_size, stride, padding, dilation)

print("Input Tensor Shape:", input_tensor.shape)
print("Unfolded Tensor Shape:", unfolded_tensor.shape)
print("Unfolded Tensor:\n", unfolded_tensor)
import torch

# Define input tensor and parameters for Unfold
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size=1, Channels=3, Height=4, Width=4
kernel_size = (2, 2)
stride = (1, 1)
padding = (0, 0)

# Create an instance of Unfold
unfold = torch.nn.Unfold(kernel_size, stride, padding)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Output shape should be [1, 12, 9] (Batch size*Channels*kernel_size[0]*kernel_size[1], (Height+2*Padding-kernel_size[0])/Stride[0]+1, (Width+2*Padding-kernel_size[1])/Stride[1]+1)
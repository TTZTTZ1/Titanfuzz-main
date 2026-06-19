import torch
from torch.autograd import Variable

# Create a random input tensor
input_tensor = Variable(torch.randn(1, 3, 4, 5, 6))

# Define the Conv3d layer
conv_layer = torch.nn.Conv3d(in_channels=3, out_channels=8, kernel_size=(2, 3, 4), stride=(1, 1, 1), padding=(1, 1, 1), groups=1, bias=True, padding_mode='zeros')

# Apply the convolution
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)
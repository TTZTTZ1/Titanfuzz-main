import torch
import torch.nn as nn

# Define a simple model using ConvTranspose1d
class SimpleUpsampler(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels, out_channels, kernel_size, stride=stride, padding=padding)

    def forward(self, x):
        return self.conv_transpose(x)

# Example usage
if __name__ == "__main__":
    # Create an instance of the model
    upsampler = SimpleUpsampler(in_channels=16, out_channels=8, kernel_size=4, stride=2, padding=1)
    
    # Generate random input tensor
    input_tensor = torch.randn(1, 16, 5)
    
    # Perform the forward pass
    output_tensor = upsampler(input_tensor)
    
    print("Input shape:", input_tensor.shape)
    print("Output shape:", output_tensor.shape)
import torch
from torch import nn

# Define a simple Convolutional Neural Network using torch.nn.Conv2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Create a convolutional layer with 1 input channel, 3 output channels, kernel size of 3x3
        self.conv = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3)

    def forward(self, x):
        return self.conv(x)

# Example usage
if __name__ == "__main__":
    # Create an instance of the CNN
    cnn = SimpleCNN()
    
    # Create a random input tensor with shape (batch_size, in_channels, height, width)
    input_tensor = torch.randn(1, 1, 5, 5)  # Batch size of 1, 1 input channel, 5x5 image
    
    # Forward pass through the network
    output_tensor = cnn(input_tensor)
    
    print("Input Tensor Shape:", input_tensor.shape)
    print("Output Tensor Shape:", output_tensor.shape)
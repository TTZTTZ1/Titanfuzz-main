import torch
import torch.nn as nn

# Define a simple Convolutional Neural Network layer using torch.nn.Conv2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Create a convolutional layer with 1 input channel, 32 output channels, kernel size of 3x3
        self.conv_layer = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3)

    def forward(self, x):
        return self.conv_layer(x)

# Example usage
if __name__ == "__main__":
    # Create an instance of the CNN
    cnn = SimpleCNN()
    
    # Create a random input tensor with shape (batch_size, in_channels, height, width)
    input_tensor = torch.randn(1, 1, 28, 28)  # Batch size of 1, 1 channel, 28x28 image
    
    # Forward pass through the network
    output = cnn(input_tensor)
    
    print(output.shape)  # Should print: torch.Size([1, 32, 26, 26])
import torch
from torch import nn

# Define a simple Convolutional Neural Network using torch.nn.Conv2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Create a convolutional layer with 1 input channel, 3 output channels, kernel size of 3x3
        self.conv = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3)

    def forward(self, x):
        # Pass the input through the convolutional layer
        return self.conv(x)

# Example usage:
if __name__ == "__main__":
    # Create an instance of the CNN
    model = SimpleCNN()
    
    # Create a random input tensor with shape (batch_size, in_channels, height, width)
    input_tensor = torch.randn(1, 1, 28, 28)  # Batch size of 1, 1 input channel, 28x28 image
    
    # Forward pass through the model
    output = model(input_tensor)
    
    print("Output shape:", output.shape)
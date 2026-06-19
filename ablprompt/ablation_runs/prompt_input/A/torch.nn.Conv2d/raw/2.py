import torch
import torch.nn as nn

# Define a simple Convolutional Neural Network layer using torch.nn.Conv2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Create a convolutional layer with 1 input channel, 32 output channels, kernel size of 3x3, and stride of 1
        self.conv_layer = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1)

    def forward(self, x):
        # Pass the input through the convolutional layer
        return self.conv_layer(x)

# Example usage
if __name__ == "__main__":
    # Create an instance of the CNN
    cnn = SimpleCNN()
    
    # Create a random input tensor with shape (batch_size, in_channels, height, width)
    input_tensor = torch.randn(1, 1, 28, 28)  # Batch size of 1, 1 input channel, 28x28 image
    
    # Forward pass through the network
    output_tensor = cnn(input_tensor)
    
    print("Input Tensor Shape:", input_tensor.shape)
    print("Output Tensor Shape:", output_tensor.shape)
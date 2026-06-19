import torch
import torch.nn as nn

# Define a simple model using Conv2d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        # Create a convolutional layer with 1 input channel, 3 output channels, kernel size of 3x3
        self.conv = nn.Conv2d(1, 3, kernel_size=3)

    def forward(self, x):
        return self.conv(x)

# Example usage
if __name__ == "__main__":
    # Create an instance of the model
    model = SimpleConvModel()
    
    # Create a random input tensor with shape (batch_size, channels, height, width)
    input_tensor = torch.randn(1, 1, 5, 5)  # Batch size of 1, 1 channel, 5x5 image
    
    # Forward pass through the model
    output_tensor = model(input_tensor)
    
    print("Input Tensor Shape:", input_tensor.shape)
    print("Output Tensor Shape:", output_tensor.shape)
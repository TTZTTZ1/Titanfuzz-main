import torch
import torch.nn as nn

# Define a simple model using LayerNorm
class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(SimpleModel, self).__init__()
        self.layer_norm = nn.LayerNorm(hidden_size)

    def forward(self, x):
        return self.layer_norm(x)

# Example usage
if __name__ == "__main__":
    batch_size = 10
    input_size = 20
    hidden_size = 30
    
    # Create a random input tensor
    input_tensor = torch.randn(batch_size, hidden_size)
    
    # Initialize the model
    model = SimpleModel(input_size, hidden_size)
    
    # Forward pass through the model
    output = model(input_tensor)
    
    print("Input Tensor Shape:", input_tensor.shape)
    print("Output Tensor Shape:", output.shape)
    print("LayerNorm Output:", output)
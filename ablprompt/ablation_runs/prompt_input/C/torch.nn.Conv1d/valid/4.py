import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConv1dModel(nn.Module):
    def __init__(self):
        super(SimpleConv1dModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)
    
    def forward(self, x):
        return self.conv1(x)

# Create an instance of the model
model = SimpleConv1dModel()

# Generate some random input data
input_data = torch.randn(20, 16, 50)

# Forward pass through the model
output_data = model(input_data)

print("Input Shape:", input_data.shape)
print("Output Shape:", output_data.shape)
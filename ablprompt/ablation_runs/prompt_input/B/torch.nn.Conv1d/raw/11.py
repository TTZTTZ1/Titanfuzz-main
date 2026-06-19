import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=1, bias=True, padding_mode='zeros')
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        return x

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Initialize the model and move it to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleModel().to(device)
input_tensor = input_tensor.to(device)

# Forward pass
output = model(input_tensor)
print(output.shape)
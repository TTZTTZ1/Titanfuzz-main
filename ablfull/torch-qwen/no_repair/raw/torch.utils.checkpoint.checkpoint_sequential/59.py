import torch
import torch.nn as nn

# Define some sample layers
class Layer1(nn.Module):
    def forward(self, x):
        return x * 2

class Layer2(nn.Module):
    def forward(self, x):
        return x + 3

# Create a sequential model or list of layers
model = nn.Sequential(Layer1(), Layer2())
functions = [Layer1(), Layer2()]  # Alternatively, you can use `model.children()` for a real-world scenario

# Set up input data
input_tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=2, input=input_tensor)

print(output)
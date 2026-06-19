import torch
import torch.nn as nn

# Define a simple model using torch.nn.Linear
class SimpleModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        return self.linear(x)

# Example usage
input_size = 10
output_size = 5
model = SimpleModel(input_size, output_size)
input_data = torch.randn(32, input_size)  # Batch size of 32
output = model(input_data)
print(output.shape)  # Should print: torch.Size([32, 5])
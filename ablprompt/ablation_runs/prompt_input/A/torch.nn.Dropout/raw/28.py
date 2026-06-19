import torch
import torch.nn as nn

# Create a simple model with Dropout layer
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.dropout = nn.Dropout(p=0.5)
    
    def forward(self, x):
        return self.dropout(x)

# Example usage
model = SimpleModel()
input_tensor = torch.randn(10, 3)  # Batch size of 10, input features of 3
output_tensor = model(input_tensor)
print(output_tensor)
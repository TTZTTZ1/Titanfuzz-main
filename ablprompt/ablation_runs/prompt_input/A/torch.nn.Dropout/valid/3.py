import torch
import torch.nn as nn

# Create a simple model with Dropout
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.dropout = nn.Dropout(p=0.5)
        self.fc = nn.Linear(10, 2)

    def forward(self, x):
        x = self.dropout(x)
        return self.fc(x)

# Example usage of the model
model = SimpleModel()
input_data = torch.randn(32, 10)  # Batch size of 32, input features of 10
output = model(input_data)
print(output.shape)  # Should be [32, 2]
import torch
from torch.nn import LayerNorm

# Example usage of LayerNorm in a complex way
class ComplexModel(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ComplexModel, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.ln1 = LayerNorm(hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.ln1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Create an instance of the model and run a forward pass
model = ComplexModel(input_size=10, hidden_size=20, output_size=3)
input_data = torch.randn(5, 10)  # Batch size of 5, input size of 10
output = model(input_data)
print(output.shape)  # Should be [5, 3]
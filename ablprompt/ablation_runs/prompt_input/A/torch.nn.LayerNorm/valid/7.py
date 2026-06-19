import torch

# Define a simple model with LayerNorm
class SimpleModel(torch.nn.Module):
    def __init__(self, input_size, hidden_size):
        super(SimpleModel, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.ln = torch.nn.LayerNorm(hidden_size)
        self.fc2 = torch.nn.Linear(hidden_size, input_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.ln(x)
        x = self.fc2(x)
        return x

# Example usage of the model
input_size = 10
hidden_size = 20
model = SimpleModel(input_size, hidden_size)

# Create a random input tensor
input_tensor = torch.randn(5, input_size)  # batch size of 5

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor)
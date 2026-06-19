import torch

# Define a simple model with LayerNorm
class SimpleModel(torch.nn.Module):
    def __init__(self, input_size, hidden_size):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(input_size, hidden_size)
        self.layer_norm = torch.nn.LayerNorm(hidden_size)

    def forward(self, x):
        x = self.linear(x)
        x = self.layer_norm(x)
        return x

# Example usage
input_tensor = torch.randn(10, 20)  # Batch size of 10, feature size of 20
model = SimpleModel(20, 30)
output = model(input_tensor)
print(output.shape)  # Should print: torch.Size([10, 30])
import torch

# Define a simple model with LayerNorm
class SimpleModel(torch.nn.Module):
    def __init__(self, input_size):
        super(SimpleModel, self).__init__()
        self.layer_norm = torch.nn.LayerNorm(input_size)

    def forward(self, x):
        return self.layer_norm(x)

# Example usage
model = SimpleModel(10)
input_tensor = torch.randn(5, 10)  # Batch size of 5, input size of 10
output_tensor = model(input_tensor)
print(output_tensor)
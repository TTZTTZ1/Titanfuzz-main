import torch

# Define some dummy neural network layers
class DummyLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x):
        return self.linear(x)

layer1 = DummyLayer()
layer2 = DummyLayer()

# Create a sequential model
sequential_model = torch.nn.Sequential(layer1, layer2)

# Prepare input data
input_data = torch.randn(5, 10)

# Call the checkpoint_sequential function
output = torch.utils.checkpoint.checkpoint_sequential([layer1, layer2], segments=2, input=input_data)
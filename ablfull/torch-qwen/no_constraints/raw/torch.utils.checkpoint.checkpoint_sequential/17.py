import torch
from torch.utils.checkpoint import checkpoint_sequential

# Define a simple module to be used as a function in checkpointing
class SimpleModule(torch.nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.fc = torch.nn.Linear(10, 10)

    def forward(self, x):
        return self.fc(x)

# Create a sequence of modules
modules = [SimpleModule(), SimpleModule()]

# Prepare input data
input_data = torch.randn(5, 10)

# Call the API
output = checkpoint_sequential(modules, segments=1, input=input_data)
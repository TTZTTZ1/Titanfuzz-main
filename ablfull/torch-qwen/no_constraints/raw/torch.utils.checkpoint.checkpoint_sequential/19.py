import torch

# Define a simple sequential function
class SimpleFunction(torch.nn.Module):
    def __init__(self):
        super(SimpleFunction, self).__init__()
        self.linear = torch.nn.Linear(5, 5)

    def forward(self, x):
        return self.linear(x)

# Create a sequence of functions
functions = [SimpleFunction(), SimpleFunction()]

# Prepare input data
input_data = torch.randn(1, 5)

# Call the checkpoint_sequential function
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=1, input=input_data)
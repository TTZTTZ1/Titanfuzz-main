import torch

# Define a simple script module
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(5, 1)

    def forward(self, x):
        return self.linear(x)

# Create an instance of the model
m = SimpleModel()

# Prepare the file path for saving
f = 'model.pt'

# Save the model using torch.jit.save
torch.jit.save(m, f)
import torch

# Create a simple ScriptModule
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

m = SimpleModel()
f = "simple_model.pt"

# Save the model to a file
torch.jit.save(m, f)
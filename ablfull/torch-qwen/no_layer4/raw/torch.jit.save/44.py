import torch

# Create a simple script module
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(5, 1)

    def forward(self, x):
        return self.linear(x)

m = SimpleModel()
f = "model.pt"

# Save the model
torch.jit.save(m, f)
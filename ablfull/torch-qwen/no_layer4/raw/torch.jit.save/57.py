import torch

# Define a simple ScriptModule
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

model = SimpleModel()
torch.jit.save(model, "simple_model.pt")
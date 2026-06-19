import torch

# Create a simple script module
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    @torch.jit.script_method
    def forward(self, x):
        return self.linear(x)

model = SimpleModel()
torch.jit.save(model, 'model.pt')
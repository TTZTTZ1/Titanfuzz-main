import torch

class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(5, 1)

    def forward(self, x):
        return self.linear(x)

model = SimpleModel()
f = 'simple_model.pt'
torch.jit.save(model, f)
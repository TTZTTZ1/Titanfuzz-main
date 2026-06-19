import torch

# Prepare a dummy script module
class DummyModel(torch.nn.Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)

m = DummyModel()
f = 'dummy_model.pt'

# Save the model
torch.jit.save(m, f)
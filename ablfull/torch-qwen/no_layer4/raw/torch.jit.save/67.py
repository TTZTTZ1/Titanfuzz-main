import torch

class SimpleModel(torch.nn.Module):
    def forward(self, x):
        return x * 2

model = SimpleModel()
f = 'simple_model.pt'
torch.jit.save(model, f)
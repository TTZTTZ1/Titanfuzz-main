import torch

class MyModel(torch.nn.Module):
    def forward(self, x):
        return x * 2

model = MyModel()
torch.jit.save(model, "my_model.pt")
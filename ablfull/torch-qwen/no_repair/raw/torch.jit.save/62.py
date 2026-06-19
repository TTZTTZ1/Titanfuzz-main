import torch

# Create a simple script module
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)

model = MyModel()
scripted_model = torch.jit.script(model)
torch.jit.save(scripted_model, "model.pt")
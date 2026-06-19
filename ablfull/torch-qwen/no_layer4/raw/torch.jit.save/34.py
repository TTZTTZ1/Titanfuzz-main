import torch

# Define a simple script module
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.linear = torch.nn.Linear(5, 3)

    def forward(self, x):
        return self.linear(x)

model = MyModel()
torch.jit.save(model, 'my_model.pt')
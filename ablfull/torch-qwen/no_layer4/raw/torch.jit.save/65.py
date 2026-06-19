import torch

# Define a simple PyTorch model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(5, 1)

    def forward(self, x):
        return self.linear(x)

model = SimpleModel()

# Save the model using torch.jit.save
torch.jit.save(model, 'example.pt')
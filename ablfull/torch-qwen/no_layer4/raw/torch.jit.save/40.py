import torch

# Create a simple script module
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()

# Save the model to a file
torch.jit.save(model, 'simple_model.pt')
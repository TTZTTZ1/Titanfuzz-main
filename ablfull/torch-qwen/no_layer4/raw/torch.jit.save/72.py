import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()

# Save the model using torch.jit.save
torch.jit.save(model, "simple_model.pt")
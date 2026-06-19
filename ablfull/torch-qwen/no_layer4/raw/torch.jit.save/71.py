import torch

# Define a simple model to script
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

# Create an instance of the model
model = SimpleModel()

# Script the model
scripted_model = torch.jit.script(model)

# Save the scripted model
torch.jit.save(scripted_model, "simple_model.pt")
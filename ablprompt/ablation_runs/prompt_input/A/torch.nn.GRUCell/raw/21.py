import torch

# Define input size, hidden size, and number of layers for GRUCell
input_size = 10
hidden_size = 20
num_layers = 1

# Create an instance of GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input tensor and hidden state
input_tensor = torch.randn(1, input_size)  # batch_size=1, input_size=input_size
hidden_state = torch.randn(1, hidden_size)  # batch_size=1, hidden_size=hidden_size

# Perform a forward pass through the GRUCell
output = gru_cell(input_tensor, hidden_state)

print(output)
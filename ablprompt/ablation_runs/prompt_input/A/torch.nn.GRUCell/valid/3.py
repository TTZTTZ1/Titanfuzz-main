import torch

# Define input size, hidden size, and number of layers for GRUCell
input_size = 10
hidden_size = 20
num_layers = 1

# Initialize GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input tensor and initial hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)

# Forward pass through GRUCell
new_hidden_state = gru_cell(input_tensor, hidden_state)

print(new_hidden_state)
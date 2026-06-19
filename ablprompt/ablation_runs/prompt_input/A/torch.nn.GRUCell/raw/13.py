import torch

# Define input and hidden state dimensions
input_size = 10
hidden_size = 20

# Initialize GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input tensor and hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)

# Perform a forward pass through the GRUCell
new_hidden_state = gru_cell(input_tensor, hidden_state)

print("New Hidden State:", new_hidden_state)
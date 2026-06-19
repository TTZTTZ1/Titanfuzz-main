import torch

# Define input size, hidden size, and number of layers for GRU
input_size = 10
hidden_size = 20
num_layers = 1

# Create an instance of GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input tensor and hidden state
input_tensor = torch.randn(1, input_size)  # Batch size of 1
hidden_state = torch.zeros(1, hidden_size)  # Initial hidden state

# Perform a single step through the GRUCell
output, new_hidden_state = gru_cell(input_tensor, hidden_state)

print("Output:", output)
print("New Hidden State:", new_hidden_state)
import torch

# Define the input size and hidden size
input_size = 10
hidden_size = 20

# Create an instance of GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_data = torch.randn(1, input_size)  # Batch size of 1
hidden_state = torch.randn(1, hidden_size)  # Batch size of 1

# Perform a forward pass through the GRUCell
new_hidden_state = gru_cell(input_data, hidden_state)

print("New Hidden State:", new_hidden_state)
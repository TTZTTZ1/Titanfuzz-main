import torch

# Define the input size and hidden size
input_size = 10
hidden_size = 20

# Create an instance of GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)

# Perform one step of GRU computation
updated_hidden_state = gru_cell(input_tensor, hidden_state)

print("Updated Hidden State:", updated_hidden_state)
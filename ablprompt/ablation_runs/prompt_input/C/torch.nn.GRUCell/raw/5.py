import torch

# Define the dimensions
input_size = 10
hidden_size = 20

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input and initial hidden state
input_data = torch.randn(5, input_size)  # Sequence length of 5
initial_hidden_state = torch.randn(hidden_size)

# Process the sequence through the GRUCell
for i in range(input_data.size(0)):
    current_input = input_data[i]
    updated_hidden_state = gru_cell(current_input, initial_hidden_state)
    initial_hidden_state = updated_hidden_state

print("Updated Hidden State:", updated_hidden_state)
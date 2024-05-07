#!/usr/bin/env ruby
# Function to find all occurrences of "^h.n$" pattern in the input string
def find_hn(input)
  input.scan(/^h.n$/)
end

# Extract the first argument from the command-line arguments
input_string = ARGV[0]

# Call the function to find occurrences and join them
puts find_hn(input_string).join

#!/usr/bin/env ruby
# Check if there's exactly one argument provided
if ARGV.length == 1
  # Regular expression to match "School"
  regex = /School/
  
  # Match the argument against the regular expression
  puts ARGV[0].match?(regex) ? ARGV[0] : ""
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

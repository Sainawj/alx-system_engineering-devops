# Puppet exec resource to increase the file descriptor limit for the holberton user
exec { 'increase file descriptor limit for holberton user':
  
  # Command to append the necessary limits to /etc/security/limits.conf
  command => 'echo "holberton soft nofile 65535" >> /etc/security/limits.conf && echo "holberton hard nofile 65535" >> /etc/security/limits.conf',
  
  # Specifying the system path to ensure the command can locate necessary binaries
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  
  # Conditional execution to avoid duplicate entries in limits.conf
  unless  => 'grep -q "holberton soft nofile 65535" /etc/security/limits.conf',
  
  # This setting increases the maximum number of open files (file descriptors)
  # for the holberton user, resolving the "Too many open files" error and
  # allowing the user to log in and open files without issues.
}

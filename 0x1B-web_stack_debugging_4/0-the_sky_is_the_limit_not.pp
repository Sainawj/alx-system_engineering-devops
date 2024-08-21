# Puppet exec resource to increase the maximum number of open file descriptors for Nginx
exec { 'increase nginx file descriptor limit':
  # Command to update the limit and restart Nginx
  command => 'sed -i "s/15/10000/" /etc/default/nginx && systemctl restart nginx',
  
  # Specifying the system path to ensure the command can locate necessary binaries
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  
  # Check if the current limit is 15 before running the command
  onlyif  => 'grep -q "15" /etc/default/nginx',
  
  # This setting increases the number of file descriptors Nginx can open, 
  # allowing it to handle more concurrent connections.
}

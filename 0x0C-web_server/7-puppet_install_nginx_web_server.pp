# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define content for index.html file
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Holberton School',
  require => Package['nginx'],
}

# Add rewrite rule in Nginx configuration
file_line { 'rewrite_redirect_me':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after    => 'server_name _;',
  multiple => true,
  require  => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

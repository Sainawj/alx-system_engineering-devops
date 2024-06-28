# This makes a file in /tmp

file { '/tmp/school':
  content =>'Puppet is awesome',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}

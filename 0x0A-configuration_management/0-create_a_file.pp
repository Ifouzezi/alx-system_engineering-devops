# Create file in directory with permissions
file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
}

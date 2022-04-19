# Requirements:
# Your SSH client configuration must be configured to use the private key ~/.ssh/school
# Your SSH client configuration must be configured to refuse to authenticate using a password

file_line { 'change password in off':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}

file_line { 'Add identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}

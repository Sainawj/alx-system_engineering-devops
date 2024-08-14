# Corrects any incorrect 'phpp' file extensions to 'php' within the WordPress configuration file 'wp-settings.php'.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',  # Executes a search and replace to fix the typo.
  path    => '/usr/local/bin/:/bin/'                                # Specifies the directories where the command should be executed.
}

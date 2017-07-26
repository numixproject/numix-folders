message('Compiling resources')
gnome.compile_resources(
  'org.Numix.Folders',
  'org.Numix.Folders.gresource.xml',
  gresource_bundle: true,
  source_dir : '.',
  install_dir : DATA_DIR,
  install: true
)

message('Preparing schemas')
install_data(
  'org.Numix.Folders.gschema.xml',
  install_dir: 'share/glib-2.0/schemas'
)

message('Making a .desktop file')
i18n.merge_file(
  input: 'org.Numix.Folders.desktop.in',
  output: 'org.Numix.Folders.desktop',
  po_dir: '../po',
  type: 'desktop',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)

message('Preparing appdata')
i18n.merge_file(
  input: 'org.Numix.Folders.appdata.xml.in',
  output: 'org.Numix.Folders.appdata.xml',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'appdata')
)

message('Making a list of icons')
subdir('icons')

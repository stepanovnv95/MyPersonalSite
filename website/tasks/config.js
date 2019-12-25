'use strict';

const PATHS = {};

PATHS.frontend_root  = './frontend';
PATHS.templates_root = './templates/website';
PATHS.static_root    = './static/website';

PATHS.manifest  = {
  base: PATHS.static_root,
  file: 'rev-manifest.json',
};
PATHS.manifest.path = `${PATHS.manifest.base}/${PATHS.manifest.file}`;

PATHS.templates = {
  src: `${PATHS.frontend_root}/templates/**/*.html`,
  base: `${PATHS.frontend_root}/templates`,
  dest: PATHS.templates_root,
};

PATHS.styles = {
  src: `${PATHS.frontend_root}/styles/**/*.scss`,
  base: PATHS.frontend_root,
  dest: PATHS.static_root,
};

PATHS.images = {
  src: `${PATHS.frontend_root}/images/**/*.{jpg,png}`,
  base: PATHS.frontend_root,
  dest: PATHS.static_root,
};

module.exports = PATHS;

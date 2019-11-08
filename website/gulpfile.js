'use strict';

const { src, dest, series, watch } = require('gulp');
const del = require('delete');
const flatten = require('gulp-flatten');


const PATHS = {
  src: './frontend',
  templates: './templates/website'
};


function clean(cb) {
  del([PATHS.templates], cb);
}


function templates(){
  return src(`${PATHS.src}/**/*.html`)
    .pipe(flatten())
    .pipe(dest(PATHS.templates))
}


const build = series(clean, templates);


exports.clean = clean;
exports.build = build;
exports.watch = function () {
  build();
  watch(
    `${PATHS.src}/**/*.*`, { events: 'all' },
    build
  );
};

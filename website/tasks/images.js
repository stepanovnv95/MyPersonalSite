'use strict';

const gulp = require('gulp');
const rev = require('gulp-rev');

function make_images(paths, manifest) {
  return function images() {
    return gulp.src(paths.src, { base: paths.base })
      .pipe( rev() )
      .pipe( gulp.dest(paths.dest) )
      .pipe( rev.manifest( manifest.path,{ base: manifest.base, merge: true }) )
      .pipe( gulp.dest(manifest.base) );
  }
}

module.exports = make_images;

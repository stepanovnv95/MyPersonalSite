'use strict';

const gulp = require('gulp');
const filter = require('gulp-filter');
const sass = require('gulp-sass');
const rev = require('gulp-rev');
const rev_replace = require('gulp-rev-replace');

function make_styles(paths, manifest) {
  return function styles() {
    return gulp.src(paths.src, { base: paths.base })
      .pipe( filter(['**', '!**/_*.*']) )
      .pipe( sass() )
      .pipe( rev_replace({ manifest: gulp.src(manifest.path, { allowEmpty: true }) }) )
      .pipe( rev() )
      .pipe( gulp.dest(paths.dest) )
      .pipe( rev.manifest( manifest.path,{ base: manifest.base, merge: true }) )
      .pipe( gulp.dest(manifest.base) );
  }
}

module.exports = make_styles;

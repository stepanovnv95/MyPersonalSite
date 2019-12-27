'use strict';

const gulp = require('gulp');
const filter = require('gulp-filter');
const sass = require('gulp-sass');
const rev = require('gulp-rev');
const rev_replace = require('gulp-rev-replace');
const plumber = require('gulp-plumber');
const notify = require('gulp-notify');
const sourcemaps = require('gulp-sourcemaps');

function make_styles(paths, manifest) {
  return function styles() {
    return gulp.src(paths.src, { base: paths.base })
      .pipe( plumber({ errorHandler: notify.onError() }) )
      .pipe( filter(['**', '!**/_*.*']) )
      .pipe( sourcemaps.init() )
      .pipe( sass() )
      .pipe( sourcemaps.write() )
      .pipe( rev_replace({ manifest: gulp.src(manifest.path, { allowEmpty: true }) }) )
      .pipe( rev() )
      .pipe( gulp.dest(paths.dest) )
      .pipe( rev.manifest( manifest.path,{ base: manifest.base, merge: true }) )
      .pipe( gulp.dest(manifest.base) );
  }
}

module.exports = make_styles;

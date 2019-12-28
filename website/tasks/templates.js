'use strict';

const gulp = require('gulp');
const rev_replace = require('gulp-rev-replace');
const plumber = require('gulp-plumber');
const notify = require('gulp-notify');

function make_templates(paths, manifest) {
  return function templates() {
    return gulp.src(paths.src)
      .pipe( plumber({ errorHandler: notify.onError() }) )
      .pipe( rev_replace({ manifest: gulp.src(manifest.path, { allowEmpty: true }) }) )
      .pipe( gulp.dest(paths.dest) );
  }
}

module.exports = make_templates;

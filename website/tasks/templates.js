'use strict';

const gulp = require('gulp');
const filter = require('gulp-filter');
const ejs = require("gulp-ejs");
const rev_replace = require('gulp-rev-replace');
const plumber = require('gulp-plumber');
const notify = require('gulp-notify');

function make_templates(paths, manifest) {
  return function templates() {
    return gulp.src(paths.src)
      .pipe( plumber({ errorHandler: notify.onError() }) )
      .pipe( filter(['**', '!**/_*.*']) )
      .pipe( ejs() )
      .pipe( rev_replace({ manifest: gulp.src(manifest.path, { allowEmpty: true }) }) )
      .pipe( gulp.dest(paths.dest) );
  }
}

module.exports = make_templates;

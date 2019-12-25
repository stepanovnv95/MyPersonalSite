'use strict';

const gulp = require('gulp');
const filter = require('gulp-filter');
const ejs = require("gulp-ejs");
const rev_replace = require('gulp-rev-replace');

function make_templates(paths, manifest) {
  return function templates() {
    return gulp.src(paths.src)
      .pipe( filter(['**', '!**/_*.*']) )
      .pipe( ejs() )
      .pipe( rev_replace({ manifest: gulp.src(manifest.path, { allowEmpty: true }) }) )
      .pipe( gulp.dest(paths.dest) );
  }
}

module.exports = make_templates;

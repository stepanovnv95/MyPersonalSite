'use strict';

const gulp = require('gulp');
const PATHS = require('./tasks/config');


const clean = require('./tasks/clean')([PATHS.templates_root, PATHS.static_root]);
gulp.task('clean', clean);


const templates = require('./tasks/templates')(PATHS.templates, PATHS.manifest);
const styles = require('./tasks/styles')(PATHS.styles, PATHS.manifest);
const images = require('./tasks/images')(PATHS.images, PATHS.manifest);
const build_series = gulp.series(images, styles, templates);
gulp.task('build', gulp.series(clean, build_series));


function watch() {
  gulp.watch(PATHS.images.src, build_series);
  gulp.watch(PATHS.styles.src, build_series);
  gulp.watch(PATHS.templates.src, gulp.series(templates))
}
gulp.task('watch', gulp.series(clean, build_series, watch));

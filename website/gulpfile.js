'use strict';

const gulp = require('gulp');
const PATHS = require('./tasks/config');


const clean = require('./tasks/clean')([PATHS.templates_root, PATHS.static_root]);
gulp.task('clean', clean);


const templates = require('./tasks/templates')(PATHS.templates, PATHS.manifest);
const styles = require('./tasks/styles')(PATHS.styles, PATHS.manifest);
const images = require('./tasks/images')(PATHS.images, PATHS.manifest);
gulp.task('build', gulp.series(images, styles, templates));
gulp.task('rebuild', gulp.series(clean, 'build'));


const browser_sync = require("browser-sync").create();
gulp.task('serve', function () {
  browser_sync.init({
    proxy: "http://127.0.0.1:8000"
  });
  browser_sync.watch([PATHS.static_root, PATHS.templates_root])
    .on('change', browser_sync.reload);
});


function watch() {
  gulp.watch(PATHS.images.src, gulp.series('build'));
  gulp.watch(PATHS.styles.src, gulp.series('build'));
  gulp.watch(PATHS.templates.src, gulp.series(templates))
}
gulp.task('watch', gulp.series('rebuild', watch));

gulp.task('dev', gulp.series('rebuild', gulp.parallel('watch', 'serve')));

'use strict';

const gulp = require('gulp');
const PATHS = require('./tasks/config');


const clean = require('./tasks/clean')([PATHS.templates_root, PATHS.static_root]);
gulp.task('clean', clean);


const templates = require('./tasks/templates')(PATHS.templates, PATHS.manifest);
const styles = require('./tasks/styles')(PATHS.styles, PATHS.manifest);
const images = require('./tasks/images')(PATHS.images, PATHS.manifest);
gulp.task('build', gulp.series(clean, images, styles, templates));

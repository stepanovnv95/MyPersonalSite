'use strict';

const del = require('del');

function make_clean(paths) {
  return function clean(cb) {
    return del(paths, cb);
  }
}

module.exports = make_clean;

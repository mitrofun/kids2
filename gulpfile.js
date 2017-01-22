'use strict';

const gulp = require('gulp');
const sass = require('gulp-sass');
const sourcemaps = require('gulp-sourcemaps');
const rename = require('gulp-rename');
const jsmin = require('gulp-jsmin');

gulp.task('min-js', function () {
 return gulp.src('./src/static/src/js/main.js')
        .pipe(jsmin())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./src/static/src/js/'));
});

gulp.task('sass', function () {
 return gulp.src('./src/static/src/sass/**/*.scss')
  .pipe(sourcemaps.init())
  .pipe(sass().on('error', sass.logError))
  .pipe(sourcemaps.write())
  .pipe(gulp.dest('./src/static/src/css'));
});

gulp.task('sass-prod', function () {
 return gulp.src('./src/static/src/sass/**/*.scss')
  .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
  .pipe(rename({suffix: '.min'}))
  .pipe(gulp.dest('./src/static/src/css'));

});

gulp.task('watch', function() {
  gulp.watch('./src/static/src/sass/**/*.scss', gulp.series('sass'));

});

gulp.task('fonts', function() {
  return gulp.src('./src/static/src/vendors/bootstrap-sass/assets/fonts/**/*')
      .pipe(gulp.dest('./src/static/src/fonts/'))

});

gulp.task('dev', gulp.series('fonts', 'sass'));
gulp.task('prod', gulp.series('fonts', 'sass-prod', 'min-js'));
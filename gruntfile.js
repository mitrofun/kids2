module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        less: {
            options: {
                expand: true
            },
            development: {
                options: {
                    strictMath: true
                },
                files: {
                    'src/static/dist/css/main.css': ['src/static/assets/less/style.less']
                }
            },
            production: { // Target
                options: {
                    compress: true,
                    yuicompress: true,
                    optimization: 2
                },
                files: {
                    'src/static/dist/css/main.min.css': ['src/static/assets/less/style.less']
                }
            }
        },

        uglify: {
            options: {
                compress: {
                    drop_console: true
                }
            },
            my_target: {
                files: {
                    'src/static/dist/js/ie10-viewport-bug-workaround.min.js': ['src/static/assets/js/ie10-viewport-bug-workaround.js'],
                    'src/static/dist/js/ie-emulation-modes-warning.min.js': ['src/static/assets/js/ie-emulation-modes-warning.js']
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.registerTask('default', ['less:production', 'uglify']);
};
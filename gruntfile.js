module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        less: {
            options: {
                expand: true
            },
            dev: {
                options: {
                    strictMath: true
                },
                files: {
                    'src/static/dist/css/main.css': ['src/static/assets/less/style.less']
                }
            },
            release: { // Target
                options: {
                    strictMath: true,
                    yuicompress: true
                },
                files: {
                    'src/static/dist/css/main.css': ['src/static/assets/less/style.less']
                }
            }
        }

    });

    grunt.loadNpmTasks('grunt-contrib-less');
    
    grunt.registerTask('default', [
        'less:dev'
    ]);
};
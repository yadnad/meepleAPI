'use strict';
module.exports = function(grunt) {
    // Load all tasks
    require('load-grunt-tasks')(grunt);
    // Show elapsed time
    require('time-grunt')(grunt);

    var jsFiles = [
        'meeple/static/js/*.js'
    ];

    grunt.initConfig({

        jshint: {
            options: {
                jshintrc: '.jshintrc'
            },
            all: [
                'Gruntfile.js',
                'meeple/static/js/*.js',
                '!meeple/static/js/main.js',
            ]
        },

        sass: {
            dev: {
                files: {
                    'meeple/static/css/style.css': 'meeple/static/sass/theme.scss',
                },
            },
            build: {
                files: {
                    'meeple/static/css/style.min.css': 'meeple/static/sass/theme.scss',
                },
                options: {
                    style: 'compressed'
                },
            },
        },

        concat: {
            options: {
                separator: ';',
            },
            app: {
                src: [jsFiles],
                dest: 'meeple/static/js/main.js',
            },
        },

        uglify: {
            dist: {
                files: {
                    'static/js/main.min.js': [jsFiles]
                }
            }
        },

        autoprefixer: {
            options: {
                browsers: ['last 2 versions', 'ie 8', 'ie 9', 'android 2.3', 'android 4', 'opera 12']
            },
            dev: {
                options: {
                    map: {
                        prev: 'meeple/static/css/'
                    }
                },
                src: 'meeple/static/css/style.css'
            },
            build: {
                src: 'meeple/static/css/style.min.css'
            }
        },

        watch: {
            sass: {
                files: [
                    'meeple/static/sass/{,*/}*.{scss,sass}',
                    'meeple/static/sass/partials/pages/{,*/}*.{scss,sass}',
                ],
                tasks: ['sass:dev', 'autoprefixer:dev']
            },
            js: {
                files: [
                    jsFiles,
                    '<%= jshint.all %>'
                ],
                tasks: ['jshint', 'concat']
            },
        },

    });

    // Register tasks
    grunt.registerTask('default', [
        'dev',
    ]);
    grunt.registerTask('dev', [
        'jshint',
        'sass:dev',
        'autoprefixer:dev',
        'concat',
    ]);
    grunt.registerTask('build', [
        'jshint',
        'sass:build',
        'autoprefixer:build',
        'uglify',
    ]);
};
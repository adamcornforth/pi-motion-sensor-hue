module.exports = function(grunt) {

  grunt.initConfig({
    scp: { 
      options: {
          host: 'pi',
          username: 'pi',
          password: 'raspberry'
      },
      your_target: {
          files: [{
              cwd: './',
              src: 'src/**',
              filter: 'isFile',
              // path on the server 
              dest: '/home/pi/apps/hue/'
          }]
      },
    },
    watch: {
      files: ['src/**'],
      tasks: ['scp']
    }
  });

  grunt.loadNpmTasks('grunt-scp');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-ssh');


  grunt.registerTask('default', ['scp', 'sshexec']);

};


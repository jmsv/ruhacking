angular.module('filmderApp', [])
  .controller('FilderController', function ($scope) {
    var filmder = this;

    var testImg = 'http://via.placeholder.com/150x200'

    $scope.filmQueue = [{
      title: 'Wolf of Wall Street',
      desc: 'Money n stuff?',
      year: '2012',
      img: testImg

    }, {
      title: 'Titanic',
      desc: 'This boat won\'t sink tbh. Wait fuck where alla this water come from bihhh',
      year: '2019',
      img: testImg
    }, {
      title: 'Monsters, Inc',
      desc: 'Scary roar lmao',
      year: '1948',
      img: testImg
    }];

    $scope.currentFilm = $scope.filmQueue.pop();
    $scope.getNextFilm = function () {
      currentFilm = $scope.filmQueue.pop();
    }

  });
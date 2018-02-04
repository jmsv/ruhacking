angular.module('filmderApp', [])
  .controller('FilderController', function ($scope, $http) {
    var filmder = this;

    var testImg = 'http://via.placeholder.com/150x200'

    $scope.filmQueue = [{
      "length": "97",
      "cast": "Ellen DeGeneres, Albert Brooks,Ed O'Neill, Kaitlin Olson",
      "year": "2016",
      "title": "Finding Dory",
      "desc": "The friendly but forgetful blue tang fish, Dory, begins a search for her long-lost parents, and everyone learns a few things about the real meaning of family along the way.",
      "genre": "Animation,Adventure,Comedy",
      "trailer_url": "https://www.youtube.com/watch?v=0tkLUap7oGQ"
    }];

    $http.get('fake-response.json')
      .then(function (res) {
        var data = res.data;
        for (var i = 0; i < data.length; i++) {
          data[i].trailer_url = "https://www.youtube.com/watch?v=" + data[i].trailer_url;
          $scope.filmQueue.push(data[i])
        }

        console.log($scope.filmQueue)
      });

    $scope.currentFilm = $scope.filmQueue.pop();
    $scope.getNextFilm = function () {
      console.log("click");
      $scope.currentFilm = $scope.filmQueue.pop();
    }

  });
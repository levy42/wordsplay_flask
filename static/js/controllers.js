'use strict';

/* Controllers */

function IndexController($scope, GameService) {
    $scope.requests = [];
    $scope.me = 
    $scope.getRequests = function () {
        GameService.getRequests().then(function (requests) {
            $scope.requests = requests;
        });
    };

    $scope.getRequests();

    $scope.addRequest = function () {
        GameService.addRequest($scope.moveTime).then(function (request) {
            $scope.requests.push(request)
        });
    };
    $scope.cencelRequest = function () {
        GameService.cencelRequest().then(function (result) {
            if (result) delete $scope.requests[0]
        })
    }
}

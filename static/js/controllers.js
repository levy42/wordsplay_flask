'use strict';

/* Controllers */

function IndexController($scope, GameService) {
    $scope.requests = [];
    $scope.myRequest = null;
    $scope.timeValues = [];
    $scope.languages = [];
    $scope.getRequests = function () {
        GameService.getRequests().then(function (requests) {
            $scope.requests = requests;
        });
    };

    $scope.getGameConfigs = function () {
        GameService.gameConfigs().then(function (configs) {
            $scope.timeValues = configs[0];
            $scope.languages = configs[1];
        });
    };

    $scope.getGameConfigs();
    $scope.getRequests();

    $scope.addRequest = function () {
        GameService.addRequest($scope.moveTime, $scope.language).then(function (request) {
            request.my = true;
            $scope.myRequest = request;
            $scope.requests.push(request)
        });
    };
    $scope.cencelRequest = function () {
        GameService.cencelRequest().then(function (result) {
            var index = -1;
            if (result) {
                for (var i = 0, len = $scope.requests.length; i < len; i++) {
                    if ($scope.requests[i].my == true) {
                        index = i;
                        break;
                    }
                }
                $scope.myRequest = null;
                $scope.requests.splice(index, 1);
            }
        })
    };
    $scope.applyRequest = function (player) {
        GameService.applyRequest(player).then(function (result) {
            if (result) window.location = "/game";
        })
    }
}

function GameController($scope, GameService) {
    $scope.words = [
        [null, null, null, null, null],
        [null, null, null, null, null],
        [null, null, null, null, null],
        [null, null, null, null, null],
        [null, null, null, null, null]
    ];

}

'use strict';

angular.module('AppServices', ['ngResource'])
    .factory('GameService', ["$http", function ($http) {
        return {
            getRequests: function () {
                return $http.get("/game/requests").then(function (response) {
                    return response.data;
                })
            },
            addRequest: function (moveTime, language) {
                return $http.get("/game/create/" + moveTime + "/" + language).then(function (response) {
                    return response.data
                });
            },
            cencelRequest: function () {
                return $http.get("/game/cencel").then(function (response) {
                    return response.status == 200
                });
            },
            applyRequest: function (player) {
                return $http.get("/game/apply/" + player).then(function (response) {
                    return response.status == 200
                });
            },
            gameConfigs: function (player) {
                return $http.get("/game/configs").then(function (response) {
                    return response.data
                })
            }
        }
    }])
;




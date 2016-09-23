'use strict';

angular.module('AppServices', ['ngResource'])
    .factory('GameService', ["$http", function ($http) {
        return {
            getRequests: function () {
                return $http.get("/game/requests").then(function (response) {
                    return response.data;
                })
            },
            addRequest: function (moveTime) {
                return $http.get("/game/create/" + moveTime).then(function (responce) {
                    return responce.data
                });
            },
            cencelRequest: function () {
                return $http.get("/game/cencel").then(function (responce) {
                    return responce.status == 200
                });
            }
        }
    }])
;




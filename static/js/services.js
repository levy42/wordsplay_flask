'use strict';

angular.module('AppServices', ['ngResource'])
    .factory('GameService', ["$http", function ($http) {
        return {
            getRequests: function () {
                return $http.get("/game/requests").then(function (response) {
                    return response.data;
                })
            },
            addRequest: function () {
                var time = document.getElementsById("moveTime").value;
                return $http.get("/game/create/" + time)
            }
        }
    }])
;




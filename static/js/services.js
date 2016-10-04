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


angular.module('Auth', ['ngResource'])
    .factory('AuthService', ["$http", function ($http) {
        return {
            login: function (username, password) {
                var data = {
                    username: username,
                    password: password
                };
                return $http.post("/auth/login", data).then(function (response) {
                    if (response.data.result == true) return true;
                    else return response.data.result
                })
            },
            logout: function () {
                return $http.get("/auth/logout").then(function (response) {
                    return response.data.result
                });
            },
            register: function (username, password) {
                var data = {
                    username: username,
                    password: password
                };
                return $http.post("/auth/register", data).then(function (response) {
                    if (response.data.result == "success") return true;
                    else return response.data.result
                });
            },
            status: function () {
                return $http.get("/auth/status").then(function (response) {
                    return response.data.status
                })
            }
        }
    }]);


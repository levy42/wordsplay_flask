'use strict';

var app = angular.module('App', ['AppServices'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/ring.html',
			controller: IndexController
		})
		.when('/game', {
			templateUrl: 'static/partials/about.html',
			controller: AboutController
		})
		.when('/ring', {
			templateUrl: 'static/partials/ring.html',
			controller: PostListController
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
	}])
;

function start() {
	var name = document.getElementById("name").value;
	window.location.href = "/start/" + name
}
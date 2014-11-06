var G = {
    username: '',
    password: '',
    login: {}
};

angular.module("myApp",[]);

angular.module("myApp").controller("appCtl",function($scope,$http){
	$scope.G = G;
	$scope.G.username = 'u';
	$scope.G.password = 'p';

	$scope.login  = function(u,p){
	    $http.post('http://localhost:9998/auth/login',{a:100,b:[2,3,4],
							   u:u,p:p})
	    .then(function(d){
		    G.login = d.data;
		    console.log("GOOD" + d);
		},
		function(){
		    console.log("-BAD");
		});
	};
	$scope.testit = function(at){
	};
    });

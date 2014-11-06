var G = {
    username: 'u',
    password: 'p',
    login: {}
};

var app = angular.module("myApp",[]);

app.controller("appCtl",function($scope){
	$scope.x = 1000;
	$scope.G = G;

	$scope.login = function($http) {
	    alert( $http );
	    //	    alert("LOGIN");
	    /*
	    $http.get('/auth/login/'+G.username+'/'+G.password)
	    .success(function(){
		    alert("YES");
		})
	    .error(function(){
		    alert("NO");
		})
	    */
	}

    });

/*
function login() {
    console.log("login");
    var q  = $.ajax({
	    url:'localhost:9999'
	});
}

function verify() {
    console.log("verify");
}

*/

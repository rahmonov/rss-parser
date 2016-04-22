(function () {
    'use strict';

    angular
        .module('digest')
        .factory('categoryModel', categoryModel);

    categoryModel.$inject = ['$http', '$q'];

    /** @ngInject */
    function categoryModel($http, $q) {

        var service = {
            getAll: getAll,
            filter: filter
        };

        return service;

        function getAll() {
            var request = $http({
                method: "get",
                url: "api/categories"
            });

            return (request.then(handleSuccess, handleError));
        }

        function filter(catName) {
            var request = $http({
                method: "get",
                url: "api/categories/",
                params: {
                    catName: capitalizeFirstLetter(catName)
                }
            });

            return (request.then(handleSuccess, handleError));
        }

        function handleError(response) {
            if (
                !angular.isObject(response.data) || !response.data.message
            ) {
                return ($q.reject("An unknown error occurred."));
            }
            // Otherwise, use expected error message.
            return ($q.reject(response.data.message));
        }

        function handleSuccess(response) {
            return(response.data);
        }

        function capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
        }
    }
})();

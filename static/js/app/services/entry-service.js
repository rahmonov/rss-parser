(function () {
    'use strict';

    angular
        .module('digest')
        .factory('entryModel', entryModel);

    entryModel.$inject = ['$http', '$q'];

    /** @ngInject */
    function entryModel($http, $q) {

        var service = {
            getAll: getAll,
            filter: filter,
            report: report
        };

        return service;

        function getAll() {
            var request = $http({
                method: "get",
                url: "api/entries"
            });

            return (request.then(handleSuccess, handleError));
        }

        function filter(fromDate, toDate, categoryId) {
            var request = $http({
                method: "get",
                url: "api/entries/filter",
                params: {
                    fromDate: JSON.stringify(fromDate),
                    toDate: JSON.stringify(toDate),
                    categoryId: categoryId
                }
            });

            return (request.then(handleSuccess, handleError));
        }

        function report(email, entryIds) {
            var request = $http({
                method: "post",
                url: "api/entries/report/",
                data: {
                    email: email,
                    entryIds: entryIds
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
    }
})();
